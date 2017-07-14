

## send keys
def sendKeysByTinyMCE(testData, text):
    driver = testData['driver']
    logger = testData['logger']
    try:
        driver.execute_script("tinyMCE.activeEditor.selection.setContent('" + text + "')")
        logger.passed("Sent '%s' to the TinyMCE widget")
        return "PASSED"
    except Exception as e:
        logger.error(str(e))
        actionsOnFail.performActions(testData)
        return "FAILED"

## click


## cannot click/select

def verifyNotClickableByXPath(testData, xpath):
    driver = testData['driver']
    logger = testData['logger']
    try:
        if not driver.find_element_by_xpath(xpath).click():
            logger.passed("Could not click on xpath: %s" % xpath)
            return "PASSED"
        else:
            logger.failed("Clicked element at xpath '%s' - element should not be available" % (xpath))
            return "FAILED"
    except Exception as e:
        logger.failed("Element at xpath: %s cannot be found" % xpath)
        logger.failed(str(e))
        actionsOnFail.performActions(testData)
        return "FAILED"














########################## DROP DOWN FIELD FUNCTIONS ##############################

# new drop down selector
def selectDropDownItemByID(testData, dropDownID, itemText):
    driver = testData['driver']
    logger = testData['logger']
    try:
        select = Select(driver.find_element_by_id(dropDownID))
        logger.info("Dropdown with id '%s' found" % dropDownID)
    except Exception as e:
        logger.error(str(e))
        logger.error("Could not find the dropdown menu at id '%s'" % dropDownID)
        actionsOnFail.exitTestScriptGracefully(testData)
    try:
        select.select_by_visible_text(itemText)
        logger.passed("'%s' selected from drop down '%s'" % (itemText, dropDownID))
        return "PASSED"
    except Exception as e:
        logger.error(str(e))
        logger.error("Error selecting the correct option '%s' from drop down '%s'" % (itemText, dropDownID))
        logger.info("The dropdown contents were: " + [str(o.text) for o in
                                                      select.options])  ## this can potentially take a long time to execute
        actionsOnFail.exitTestScriptGracefully(testData)


# Select drop down item by value attribute
def selectDropDownItemByID_Attribute(testData, dropDownID, itemValue):
    driver = testData['driver']
    logger = testData['logger']
    try:
        Select(driver.find_element_by_id(dropDownID))
    # logger.info( [str(o.value) for o in select.options] )
    except Exception as e:
        logger.error(str(e))
        logger.error("Could not find the dropdown menu at id '%s'" % dropDownID)
        actionsOnFail.exitTestScriptGracefully(testData)
    try:
        Select(driver.find_element_by_value(itemValue))
        logger.passed("'%s' selected from drop down '%s'" % (itemValue, dropDownID))
        return "PASSED"
    except Exception as e:
        logger.error(str(e))
        logger.error("Error selecting the correct option '%s' from drop down '%s'" % (itemValue, dropDownID))
        actionsOnFail.exitTestScriptGracefully(testData)


def selectDropDownItemByIDOld(testData, dropDownID, itemText):
    driver = testData['driver']
    logger = testData['logger']
    try:
        driver.find_element_by_id(dropDownID).click()
        pause(testData, testData['dropDownExpandPause'])
    except Exception as e:
        logger.error(str(e))
        logger.error("There was an ERROR locating the dropdown box dropDownID '%s'" % dropDownID)
        actionsOnFail.exitTestScriptGracefully(testData)
    dropDown = driver.find_element_by_id(dropDownID)
    itemTextFound = False
    try:
        for option in dropDown.find_elements_by_tag_name('option'):
            logger.info("Option = '%s' // Looking for '%s'" % (option.text, itemText))
            if itemText in option.text:
                mouseOverByXPath(testData, option)
                option.click()
                logger.info("Clicked to open drop down '%s'" % dropDownID)
                pause(testData, testData['dropDownExpandPause'])
                itemTextFound = True
                break
    except Exception as e:
        logger.error(str(e))
        logger.error(
            "There was an ERROR collecting options from the dropdown box dropDownID '%s' or selecting option '%s'" % (
            dropDownID, itemText))
        actionsOnFail.exitTestScriptGracefully(testData)
    if itemTextFound == True:
        logger.passed("Option '%s' was found and selected" % itemText)
        return "PASSED"
    else:
        logger.failed("Option '%s' could not be found in drop down '%s'" % (itemText, dropDownID))
        actionsOnFail.exitTestScriptGracefully(testData)


def selectDropDownItemByXPath(testData, dropDownXPath, itemText):
    driver = testData['driver']
    logger = testData['logger']
    try:
        driver.find_element_by_xpath(dropDownXPath).click()
        pause(testData, testData['dropDownExpandPause'])
    except Exception as e:
        logger.error(str(e))
        logger.error("There was an ERROR locating the dropdown box dropDownXPath '%s'" % dropDownXPath)
        actionsOnFail.exitTestScriptGracefully(testData)
    dropDown = driver.find_element_by_xpath(dropDownXPath)
    itemTextFound = False
    logger.info("'%s' options found in drop down xpath '%s'" % (
    len(dropDown.find_elements_by_tag_name('option')), dropDownXPath))
    try:
        for option in dropDown.find_elements_by_tag_name('option'):
            logger.info("Option = '%s' // Looking for '%s'" % (option.text, itemText))
            if itemText in option.text:
                option.click()
                logger.info("Clicked to open drop down '%s'" % dropDownXPath)
                pause(testData, testData['dropDownExpandPause'])
                itemTextFound = True
                break
    except Exception as e:
        logger.error(str(e))
        logger.error(
            "There was an ERROR collecting options from the dropdown box dropDownXPath '%s' or selecting option '%s'" % (
            dropDownXPath, itemText))
        actionsOnFail.exitTestScriptGracefully(testData)
    if itemTextFound == True:
        logger.passed("Option '%s' was found and selected" % itemText)
        return "PASSED"
    else:
        logger.failed("Option '%s' could not be found in drop down '%s'" % (itemText, dropDownXPath))
        actionsOnFail.exitTestScriptGracefully(testData)


def selectDropDownItemByCSS(testData, dropDownCSS, itemText):
    driver = testData['driver']
    logger = testData['logger']
    try:
        driver.find_element_by_css_selector(dropDownCSS).click()
        pause(testData, testData['dropDownExpandPause'])
    except Exception as e:
        logger.error(str(e))
        logger.error("There was an ERROR locating the dropdown box dropDownCSS '%s'" % dropDownCSS)
        actionsOnFail.exitTestScriptGracefully(testData)
    dropDown = driver.find_element_by_css_selector(dropDownCSS)
    itemTextFound = False
    try:
        for option in dropDown.find_elements_by_tag_name('option'):
            logger.info("Option = '%s' // Looking for '%s'" % (option.text, itemText))
            if itemText in option.text:
                option.click()
                logger.info("Clicked to open drop down '%s'" % dropDownCSS)
                pause(testData, testData['dropDownExpandPause'])
                itemTextFound = True
                break
    except Exception as e:
        logger.error(str(e))
        logger.error(
            "There was an ERROR collecting options from the dropdown box dropDownCSS '%s' or selecting option '%s'" % (
            dropDownCSS, itemText))
        actionsOnFail.exitTestScriptGracefully(testData)
    if itemTextFound == True:
        logger.passed("Option '%s' was found and selected" % itemText)
        return "PASSED"
    else:
        logger.failed("Option '%s' could not be found in drop down '%s'" % (itemText, dropDownCSS))
        actionsOnFail.exitTestScriptGracefully(testData)


def selectDropDownItemByName(testData, dropDownName, itemText):
    driver = testData['driver']
    logger = testData['logger']
    try:
        driver.find_element_by_name(dropDownName).click()
        pause(testData, testData['dropDownExpandPause'])
    except Exception as e:
        logger.error(str(e))
        logger.error("There was an ERROR locating the dropdown box dropDownName '%s'" % dropDownName)
        actionsOnFail.exitTestScriptGracefully(testData)
    dropDown = driver.find_element_by_name(dropDownName)
    itemTextFound = False
    try:
        for option in dropDown.find_elements_by_tag_name('option'):
            logger.info("Option = '%s' // Looking for '%s'" % (option.text, itemText))
            if itemText in option.text:
                option.click()
                logger.info("Clicked to open drop down '%s'" % dropDownName)
                pause(testData, testData['dropDownExpandPause'])
                itemTextFound = True
                break
    except Exception as e:
        logger.error(str(e))
        logger.error(
            "There was an ERROR collecting options from the dropdown box dropDownName '%s' or selecting option '%s'" % (
            dropDownName, itemText))
        actionsOnFail.exitTestScriptGracefully(testData)
    if itemTextFound == True:
        logger.passed("Option '%s' was found and selected" % itemText)
        return "PASSED"
    else:
        logger.failed("Option '%s' could not be found in drop down '%s'" % (itemText, dropDownName))
        actionsOnFail.exitTestScriptGracefully(testData)


def selectDropDownItemByDescription(testData, fieldId, dropDownItemDesc):
    driver = testData['driver']
    logger = testData['logger']
    try:
        Select(driver.find_element_by_id(fieldId)).select_by_visible_text(dropDownItemDesc)
        logger.passed("Option '%s' has been found in the drop down" % dropDownItemDesc)
        return "PASSED"
    except Exception as e:
        logger.error(str(e))
        logger.error("There was an ERROR locating the item by description '%s'" % dropDownItemDesc)
        actionsOnFail.exitTestScriptGracefully(testData)
        return "ERROR"


############################### STORE FUNCTIONS ###################################













