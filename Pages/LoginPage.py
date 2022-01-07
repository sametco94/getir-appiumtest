import APPdemotest.CustomLogger as cl
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class LoginPageClass:
    log = cl.customlogger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    countrycode = "com.getir:id/signin_countryCodeTextInputLayoutMask"
    phonenumber = "com.getir:id/signin_phoneTextInputLayout"
    phoneloginbutton = "com.getir:id/signin_signInButton"
    fbloginbutton = "com.getir:id/social_facebookButton"
    googleloginbutton = "com.getir:id/social_googleButton"
    registerbutton = "com.getir:id/signUpTextView"

    def waitforelement(self, locatorvalue, locatortype):
        locatortype = locatortype.lower()
        element = None
        wait = WebDriverWait(self.driver, 25, poll_frequency=1, 
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, 
                                                 NoSuchElementException])
        if locatortype == "id":
            element = wait.until(lambda x: x.find_element_by_idlocatorvalue)
            return element
        elif locatortype == "class":
            element = wait.until(lambda x: x.find_element_by_class_namelocatorvalue)
            return element
        elif locatortype == "des":
            element = wait.until(
                lambda x: x.find_element_by_android_uiautomator('UiSelector().description("%s")' % locatorvalue))
            return element
        elif locatortype == "index":
            element = wait.until(
                lambda x: x.find_element_by_android_uiautomator("UiSelector().index(%d)" % locatorvalue))
            return element
        elif locatortype == "text":
            element = wait.until(lambda x: x.find_element_by_android_uiautomator('text("%s")' % locatorvalue))
            return element
        elif locatortype == "xpath":
            element = wait.until(lambda x: x.find_element_by_xpath('%s' % locatorvalue))
            return element
        else:
            self.log.info("Locator value " + locatorvalue + "not found")

        return element

    def getelement(self, locatorvalue, locatortype="id"):
        element = None
        try:
            locatortype = locatortype.lower()
            element = self.waitforelement(locatorvalue, locatortype)
            self.log.info("Element found with locatortype: " + locatortype + " with the locatorvalue :" + locatorvalue)
        except:
            self.log.info(
                "Element not found with locatortype: " + locatortype + " and with the locatorvalue :" + locatorvalue)

        return element

    def clickelement(self, locatorvalue, locatortype="id"):
        element = None
        try:
            locatortype = locatortype.lower()
            element = self.getelement(locatorvalue, locatortype)
            element.click()
            self.log.info(
                "Clicked on Element with locatortype: " + locatortype + " and with the locatorvalue :" + locatorvalue)
        except:
            self.log.info(
                "Unable to click on Element with locatortype: " + locatortype + " and with the locatorvalue :" + locatorvalue)

    def sendtext(self, text, locatorvalue, locatortype="id"):
        element = None
        try:
            locatortype = locatortype.lower()
            element = self.getelement(locatorvalue, locatortype)
            element.send_keys(text)
            self.log.info(
                "Send text  on Element with locatortype: " + locatortype + " and with the locatorvalue :" + locatorvalue)
        except:
            self.log.info(
                "Unable to send text on Element with locatortype: " + locatortype + " and with the locatorvalue :" + locatorvalue)

    def choose_countrycode(self, ccode):
        self.sendtext(self.countrycode, "id", ccode)
        cl.allurelogs("Country code chosen")

    def enter_phone(self, phoneno):
        self.sendtext(self.phonenumber, "id", phoneno)
        cl.allurelogs("Entered phone number")

    def click_phonelogin(self):
        self.clickelement(self.phoneloginbutton, "id")
        cl.allurelogs("Clicked on The Button for Login via Phone")

    def click_fblogin(self):
        self.clickelement(self.fbloginbutton, "id")
        cl.allurelogs("Clicked on The Button for Login via Facebook")

    def click_googlelogin(self):
        self.clickelement(self.googleloginbutton, "id")
        cl.allurelogs("Clicked on The Button for Login via Google")

    def goto_register(self):
        self.clickelement(self.registerbutton, "id")
        cl.allurelogs("Clicked onto Register")
