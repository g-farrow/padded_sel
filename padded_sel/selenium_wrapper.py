from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType


class Webdriver:

    def __init__(self, browser='firefox', platform='linux', server_url='127.0.0.1', server_port=5555, proxy=None,
                 window_size=None):
        """
        Initialise the Webdriver and return the class object, as per the provided requirements:
        :type browser: String - Browser required (e.g. firefox)
        :type platform: String - OS required (e.g. linux)
        :type server_url: String - IP/DNS of the Selenium server to start the browser on
        :type server_port: Int - Port number of the Selenium server to start the browser on
        :type proxy: String - The IP/DNS and port (: separated) of a proxy server to forward traffic through
        :type window_size: String - Desired dimensions of the browser window width by height separated by 'x'
            (e.g. "1900x1200")
        """
        self.capabilities = {'browserName': browser.lower(), 'platform': platform.upper()}
        self.command_executor = "http://{}:{}".format(server_url, server_port)
        self.window_size = window_size
        self.proxy = proxy
        if self.proxy:
            self.proxy = Proxy(
                {'proxyType': ProxyType.MANUAL, 'httpProxy': proxy, 'ftpProxy': proxy, 'sslProxy': proxy}
            )
        self.driver = webdriver.Remote(desired_capabilities=self.capabilities, command_executor=self.command_executor,
                                       proxy=proxy)
        self.delete_all_cookies()
        self.set_window_size(self.window_size)

    def quit(self):
        """
        Quit and close the running browser
        """
        self.driver.quit()

    def delete_all_cookies(self):
        """
        Remove all cookies from the running browser session
        """
        self.driver.delete_all_cookies()

    def set_window_size(self, window_size=None):
        """
        Change the size/resolution of the browser window, defaults to 'maximum'
        :type window_size: String - Desired dimensions of the browser window width by height separated by 'x'
            (e.g. "1900x1200")
        """
        if window_size:
            browser_resolution = window_size.split("x")
            self.driver.set_window_size(browser_resolution[0], browser_resolution[1])
        else:
            self.driver.maximize_window()
