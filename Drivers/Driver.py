from appium import webdriver


class Driver:

    def __init__(self):

        desired_caps = {
            "platformName": "Android",
            "platformVersion": "8",
            "deviceName": "Vestel Venus Z20",
            "app": "C:/Users/esame/Downloads/Appium and Selenium with Python From Basics to Framework/getir2104.xapk",
            "appPackage": "com.getir",
            "appActivity": "com.getir.core.feature.onboarding.OnboardingActivity"
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    def print_details(self):
        print("Current Activity", self.driver.current_activity)
        print("Current context", self.driver.current_context)
        print("Current orientation", self.driver.orientation)
        print("Check Whether device is locked or not :", self.driver.is_locked())

    def quit(self):
        self.driver.quit()
