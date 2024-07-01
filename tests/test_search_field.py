
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.run(order=5)
def test_search_field_positive(driver, login_fixture, logout_fixture):
    """ 
    This test checks the search field fith positive data.
    Here I use another fixture for login and logout to do this in right secuencess.
 
    """
    
    def wait_for_element(xpath):
        return WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))

   
    main_logo_in_the_header = wait_for_element('//div[@id="_desktop_logo"]')
    main_logo_in_the_header.click()
    wait_for_element('//input[@type="text"]').click()
    text_field = driver.find_element(By.XPATH, '//input[@type="text"]')
    text_field.clear()
    text_field.send_keys("SWEATER")
    button_search_submit = driver.find_element(By.XPATH, '//button[@type="submit"]')
    button_search_submit.click()
    wait_for_element('//*[contains(text(), "sweater")]')
     
@pytest.mark.run(order=6)
def test_search_field_negative(driver, login_fixture, logout_fixture):
    """ 
    This test checks the search field fith NEGATIVE data.
    Here I use another fixture for login and logout to do this in right secuencess.
 
    """
    
    def wait_for_element(xpath):
        return WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))

   
    main_logo_in_the_header = wait_for_element('//div[@id="_desktop_logo"]')
    main_logo_in_the_header.click()
    wait_for_element('//input[@type="text"]').click()
    text_field = driver.find_element(By.XPATH, '//input[@type="text"]')
    text_field.clear()
    text_field.send_keys("$%^&")
    button_search_submit = driver.find_element(By.XPATH, '//button[@type="submit"]')
    button_search_submit.click()
    wait_for_element('//section[@class="page-content page-not-found"]')