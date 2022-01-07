import unittest
import pytest

from APPdemotest.Pages.MainPage import MainPageClass
from APPdemotest.Pages.GETIR_Page import getirHomePage
from APPdemotest.Pages.GETIR_ProfilePage import getirProfilePage
from APPdemotest.Pages.LoginPage import LoginPageClass
from APPdemotest.Drivers.Driver import Driver


class BasicTests(unittest.TestCase):

    @pytest.mark.run
    def setUp(self):
        self.driver = Driver()

    @pytest.mark.run
    def test_basics(self):
        mainpage = MainPageClass(self.driver)
        getir_page = getirHomePage(self.driver)
        getir_profilepage = getirProfilePage(self.driver)
        loginpage = LoginPageClass(self.driver)

        mainpage.click_getir()
        getir_page.goto_profile()
        getir_profilepage.goto_login()
        loginpage.click_googlelogin()

    @pytest.mark.run
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(BasicTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
