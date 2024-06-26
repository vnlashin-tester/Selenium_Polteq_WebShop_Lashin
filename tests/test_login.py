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

def test_positive_login(driver):
     # Data
    login_email = "tester@test.com"
    login_password = "1qazxsw2"
    
    # Arrange
    
    
    # Act
    sign_in_main_page = driver.find_element(By.XPATH,  '//div[@id="_desktop_user_info"]')
    sign_in_main_page.click
    header_page_of_autorisation = driver.find_element(By.XPATH, '//header[@class="page-header"]')
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(header_page_of_autorisation))   
    email_field_autorisation = driver.find_element(By.XPATH, '//div[@class="col-md-6"]/input[@type="email"]') 
    email_field_autorisation.clear
    email_field_autorisation.send_keys(login_email)
    password_field_autorisation = driver.find_element(By.XPATH, '//input[@type="password"]')
    password_field_autorisation.clear
    password_field_autorisation.send_keys(login_password)
    button_sighn_in_form_of_autorisation = driver.find_element(By.XPATH, '//button[@id="submit-login"]') 
    button_sighn_in_form_of_autorisation.click
    header_page_witch_autorased = driver.find_element(By.XPATH, '//header[@class="page-header"]')
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(header_page_witch_autorased))

    def test_Logout_from_your_account_page():
        go_to_your_account = driver.find_element(By.XPATH, '//span[contains(text(), "Polteq Tester")]')
        go_to_your_account.click
        sign_out = driver.find_element(By.XPATH, '//a[contains(text(), "Sign out")]')
        sign_out.click
        header_page_of_autorisation = driver.find_element(By.XPATH, '//header[@class="page-header"]')
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(header_page_of_autorisation))    
    # Assert