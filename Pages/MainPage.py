import allure
from allure_commons.types import AttachmentType
import APPdemotest.CustomLogger as cl
import time


class MainPageClass:

    log = cl.customlogger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.getir = driver.find_element_by_android_uiautomator('text("getir")')
        self.getirmore = driver.find_element_by_android_uiautomator('text("getirmore")')
        self.getirfood = driver.find_element_by_android_uiautomator('text("getirfood")')
        self.getirlocals = driver.find_element_by_android_uiautomator('text("getirlocals")')
        self.getirwater = driver.find_element_by_android_uiautomator('text("getirwater")')

    def click_getir(self):
        self.getir.click()
        cl.allurelogs("Click on 'GETIR' Button")

    def click_getirmore(self):
        self.getirmore.click()
        cl.allurelogs("Click on 'GETIRMORE' Button")

    def click_getirfood(self):
        self.getir.click()
        cl.allurelogs("Click on 'GETIRFOOD' Button")

    def click_getirlocals(self):
        self.getir.click()
        cl.allurelogs("Click on 'GETIRLOCALS' Button")

    def click_getirwater(self):
        self.getir.click()
        cl.allurelogs("Click on 'GETIRWATER' Button")

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
