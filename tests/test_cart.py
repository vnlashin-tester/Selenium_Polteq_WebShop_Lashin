import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_cart(driver, login_fixture, logout_fixture):
    """ 
    This test check works with Cart.
    """
    
    def wait_for_element(xpath):
        return WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    