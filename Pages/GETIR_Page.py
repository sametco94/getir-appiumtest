import allure
from allure_commons.types import AttachmentType
import APPdemotest.CustomLogger as cl
import time


class getirHomePage:
    log = cl.customlogger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.setaddress = driver.find_element_by_android_uiautomator('text("Select Delivery Address")')
        self.homebutton = driver.find_element_by_android_uiautomator('id("com.getir:id/gabottomnavigationview_home")')
        self.searchbutton = driver.find_element_by_android_uiautomator('id("com.getir:id/gabottomnavigationview_search")')
        self.profilebutton = driver.find_element_by_android_uiautomator('id("com.getir:id/gabottomnavigationview_profile")')
        self.promotionsbutton = driver.find_element_by_android_uiautomator('id("com.getir:id/gabottomnavigationview_campaign")')

    def clickto_setaddress(self):
        self.setaddress.click()
        cl.allurelogs("Click on 'SET ADDRESS' Button")

    def goto_homepage(self):
        self.homebutton.click()
        cl.allurelogs("Click on 'HOMEPAGE' Button")

    def click_search(self):
        self.searchbutton.click()
        cl.allurelogs("Click on 'SEARCH' Button")

    def goto_profile(self):
        self.profilebutton.click()
        cl.allurelogs("Click on 'PROFILE' Button")

    def check_promotions(self):
        self.promotionsbutton.click()
        cl.allurelogs("Click on 'PROMOTIONS' Button")

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
