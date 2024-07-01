
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.run(order=3)
def test_check_one_of_item_check_box(driver, login_fixture, logout_fixture):
    """ 
    This test checks the filter. Choise only one item.
    """
    
    def wait_for_element(xpath):
        return WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))

   
    main_logo_in_the_header = wait_for_element('//div[@id="_desktop_logo"]')
    main_logo_in_the_header.click()
    
    drop_down_menu_accessories = driver.find_element(By.XPATH, '//li[@id="category-6"]')
    drop_down_menu_accessories.click()
    stationary_check_box = driver.find_element(By.XPATH, '//label[@class="facet-label"]/a[contains(text(), "Stationery")]')
    stationary_check_box.click()
    wait_for_element('//li[contains(text(), "Categories") and contains(text(), "Stationery")]')
   


@pytest.mark.run(order=4)
def test_check_two_of_items_check_box(driver, login_fixture, logout_fixture):
    """ 
    This test checks the filter. Choise TWO items.
    """
    
    def wait_for_element(xpath):
        return WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
       
    main_logo_in_the_header = wait_for_element('//div[@id="_desktop_logo"]')
    main_logo_in_the_header.click()
    
    drop_down_menu_clothes = driver.find_element(By.XPATH, '//li[@ id="category-3" ]/a[@class="dropdown-item"]')
    drop_down_menu_clothes.click()
    wait_for_element('//ul[@ class="category-sub-menu"]//a[contains(text(), "Men")]')
    
    men_check_box = driver.find_element(By.XPATH, '//label[@class="facet-label"]/a[contains(text(), "Men")]')
    men_check_box.click()
    wait_for_element('//li[contains(text(), "Categories") and contains(text(), "Men")]')
    size_L_check_box = driver.find_element(By.XPATH, '//label[@class="facet-label"]/a[contains(text(), "L")] [1]')
    size_L_check_box.click()
    wait_for_element('//li[contains(text(), "Size") and contains(text(), "L")]')
    