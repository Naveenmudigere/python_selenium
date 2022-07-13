from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class test_amz:
    def _init_(self):

        self.nav_button = '//*[@id="nav-search-submit-button"]'
        self.featured = '//*[@id="a-autoid-0-announce"]'
        self.select = '//*[@id="s-result-sort-select_2"]'

    def amazon_nav_click(self):
        self.driver.find_element(by=By.XPATH, value=self.nav_button).click()

    def amazon_feature_click(self):
        self.driver.find_element(by=By.XPATH, value=self.featured).click()

    def amazon_sort_click(self):
        self.driver.find_element(by=By.XPATH, value=self.select).click()

    def script_do(self):
        self.driver.execute_script("alert(' laptop search successfully');")
        time.sleep(4)

        self.driver.switch_to.alert.dismiss()
        print("end writting")