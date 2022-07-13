import time
import unittest
from lib2to3.pgen2 import driver

from html_test_report import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from searchlaptop import test_amz
from selenium.webdriver.common.action_chains import ActionChains


# class DemoImplicitWait():
class Testsample(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(executable_path="C:/chromedrive/chromedriver.exe")
        # time.sleep(3)

    def test_amazon(self):
        action = ActionChains(self.driver)
        self.driver.implicitly_wait(40)
        self.driver.get("https://www.amazon.in")
        titleOfWebPage = self.driver.title
        self.assertNotEqual("Amazon", titleOfWebPage, "PASSED")
        # seconds


        self.driver.maximize_window()

        # capture the title of the page
        amazon = self.driver.title
        # time.sleep(4)
        a = self.driver.find_element(by=By.XPATH, value=" //input[@id='twotabsearchtextbox']")
        action.scroll_to_element(a)
        a.send_keys("laptop")



        time.sleep(4)
        self.nav_button = "//*[@id='nav-search-submit-button']"
        self.featured = "//*[@id='a-autoid-0-announce']"
        self.select = "//*[@id='s-result-sort-select_2']"

        test_amz.amazon_nav_click(self)
        self.driver.implicitly_wait(5)
        test_amz.amazon_feature_click(self)
        self.driver.implicitly_wait(5)
        test_amz.amazon_sort_click(self)
        time.sleep(4)
        test_amz.script_do(self)

        # time.sleep(4)

    @classmethod
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
