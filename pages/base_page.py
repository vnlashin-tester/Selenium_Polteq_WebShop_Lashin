import time
import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC







class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, *locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_element(self, *locator):
        element = self.find_element(*locator)
        element.click()

    def enter_text(self, text, *locator):
        element = self.find_element(*locator)
        element.clear()
        element.send_keys(text)
