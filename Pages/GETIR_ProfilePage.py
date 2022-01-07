import allure
from allure_commons.types import AttachmentType
import APPdemotest.CustomLogger as cl
import time


class getirProfilePage:
    log = cl.customlogger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.logingbutton = driver.find_element_by_android_uiautomator('text("Login")')
        self.myaddresses = driver.find_element_by_android_uiautomator('text("My Addresses")')
        self.favproducts = driver.find_element_by_android_uiautomator('id("com.getir:id/profile_favoriteProductsConstraintLayout")')
        self.supportpage = driver.find_element_by_android_uiautomator('text("Support")')
        self.changelanguage = driver.find_element_by_android_uiautomator('id("com.getir:id/profile_languageConstraintLayout")')

    def goto_login(self):
        self.logingbutton.click()
        cl.allurelogs("Click on 'LOGIN' Button")

    def goto_myaddresses(self):
        self.myaddresses.click()
        cl.allurelogs("Click on 'MY ADDRESSES' Button")

    def goto_favs(self):
        self.favproducts.click()
        cl.allurelogs("Click on 'FAVORITE PRODUCTS' Button")

    def goto_support(self):
        self.supportpage.click()
        cl.allurelogs("Click on 'SUPPORT' Button")

    def change_language(self):
        self.changelanguage.click()
        cl.allurelogs("Click on 'LANGUAGE' Button")

    def takescreenshot(self, screenshotname):
        filename = screenshotname + "_" + (time.strftime("%d_%m_%y_%H_%M_%S")) + ".png"
        screenshotdirectory = "C:/Users/esame/PycharmProjects/screenshots for tutorial"
        screenshotpath = screenshotdirectory + filename
        try:
            self.driver.save_screenshot(screenshotpath)
            self.log.info("Screenshot save to Path : " + screenshotpath)

        except:
            self.log.info("Unable to save Screenshot to the Path : " + screenshotpath)

    def takeccreenshot(self, text):
        allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)

    def keycode(self, value):
        self.driver.press_keycode(value)
