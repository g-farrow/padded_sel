###################################################################################
#
#
###################################################################################

##################################### IMPORTS #####################################
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType


############################ DEFINE THE TEST MODULE ###################################

def createRemoteDriver(logger, nodeData):
    logger.debug("Creating driver using NODE_ADDRESS: %s, BROWSER: %s, PLATFORM: %s, WINDOW SIZE: %s, PROXY: %s" % (
        nodeData['url'], nodeData['browser'], nodeData['platform'], nodeData['window_size'],
        nodeData['webdriver_proxy']))

    caps = {'browserName': nodeData['browser'].lower(), 'platform': nodeData['platform'].upper()}
    command_exec = nodeData['url']

    # command_exec = "http://greg.farrow.rtap%40gmail.com:u04dfd9ab195c27d@hub.crossbrowsertesting.com:80/wd/hub"
    # caps = {}
    # caps['name'] = 'Win8_Firefox'
    # caps['build'] = '2.0'
    # caps['browser_api_name'] = 'FF34'
    # caps['os_api_name'] = 'Win7-C1'
    # caps['max_duration'] = '1200'
    # caps['screen_resolution'] = '1024x768'
    # caps['record_video'] = 'true'
    # caps['record_network'] = 'true'
    # caps['record_snapshot'] = 'false'

    if nodeData['webdriver_proxy'].upper() != "FALSE":  # if you are using a proxy (the config is not set to 'False')
        """ webdriver_proxy is the ip:port pairing, e.g. 192.168.22.32:9090 """
        logger.debug("Use of a proxy server is required, setting proxy to '%s'" % nodeData['webdriver_proxy'])
        proxy = Proxy({
            'proxyType': ProxyType.MANUAL,
            'httpProxy': nodeData['webdriver_proxy'],
            'ftpProxy': nodeData['webdriver_proxy'],
            'sslProxy': nodeData['webdriver_proxy']  # ,
            # 						'noProxy'	: nodeData['webdriver_proxy']
        })
        driver = webdriver.Remote(desired_capabilities=caps, command_executor=command_exec,
                                  proxy=proxy)  # create webdriver with proxy configured

    else:
        logger.debug("No proxy server identified, creating a webdriver instance without one")
        driver = webdriver.Remote(desired_capabilities=caps,
                                  command_executor=command_exec)  # create webdriver WITHOUT proxy configured
    try:
        driver.delete_all_cookies()
        logger.debug("All cookies: %s" % str(driver.get_cookies()))
        try:
            if isinstance(nodeData['window_size'], list) == True:
                driver.set_window_size(nodeData['window_size'][0], nodeData['window_size'][1])
                logger.debug("Window size set to: '%sx%s'" % (nodeData['window_size'][0], nodeData['window_size'][1]))
            elif nodeData['window_size'].upper() == "MAX":
                driver.maximize_window()
                logger.debug("Window size set to: '%s'" % nodeData['window_size'].upper())
        except:
            logger.warning(
                "Failed to set desired window size (%s), the default will be used" % str(nodeData['window_size']))

        return driver
    except Exception as e:
        logger.error(str(e))
        logger.error("Error creating remote webDriver with node_address = %s, browser = %s, platform = %s" % (
            nodeData['url'], nodeData['browser'], nodeData['platform']))


def goToWebsite(logger, driver, URL):
    try:
        driver.get(URL)
        currentURL = driver.current_url
        logger.info("Current URL is %s" % currentURL)
    except Exception as e:
        logger.error(str(e))
        logger.error("Error opening url = %s" % URL)


def quitRemoteDriver(testData):
    logger = testData['logger']
    driver = testData['driver']
    try:
        driver.quit()
    except Exception as e:
        logger.error(str(e))
        logger.error("Error closing remote webDriver")
