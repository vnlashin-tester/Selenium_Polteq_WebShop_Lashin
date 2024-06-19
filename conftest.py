#  Import:
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

@pytest.fixture
def driver():
    # ARRANGE, executed before the test starts
    driver = webdriver.Chrome()
    driver.get("https://testshop.polteq-testing.com")
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver  
    driver.quit()
