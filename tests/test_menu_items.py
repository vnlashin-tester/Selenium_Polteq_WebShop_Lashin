import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_clothes_and_submenus(driver, login_fixture, logout_fixture):
    """ 
    This test checks drop-down main menu.
    1. Clothes menu - avaliable
    2. Men-submnu avaliable. Has products and each product is avaliable.
    Women-submenu
    """
    
    def wait_for_element(xpath):
        return WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))

    main_logo_in_the_header = wait_for_element('//div[@id="_desktop_logo"]')
    main_logo_in_the_header.click()
    wait_for_element('//input[@type="text"]')
    
    # Mouse over element drop down menu clothes
    drop_down_menu_clothes = wait_for_element('//li[@id="category-3"]/a[@class="dropdown-item"]')
    ActionChains(driver).move_to_element(drop_down_menu_clothes).perform()
    wait_for_element('//li[@id="category-4"]/a[contains(text(), "Men")]')
    
    # Check that Man and Women submenus are avaliable:
    man_and_women_elements = driver.find_elements(By.XPATH, '//a[@class="dropdown-item dropdown-submenu" and contains(text(), "Women")]')
    assert len(man_and_women_elements) > 0, "Error: No submenus found with specified locator"

    # Check that Men section is visible and has content:
    submenu_drop_down_menu_clothes_men = driver.find_element(By.XPATH, '//li[@id="category-4"]/a[contains(text(), "Men")]')
    submenu_drop_down_menu_clothes_men.click()
    wait_for_element('//h1[contains(text(), "Men")]')
    time.sleep(3)
    search_field = driver.find_elements(By.XPATH, '//input[@type="text"]')
    filter_by_block = driver.find_elements(By.XPATH, '//p[contains(text(), "Filter By")]')    
    assert len(search_field) > 0, "Error: No search_field found with specified locator"
    assert len(filter_by_block) > 0, "Error: No filter_block found with specified locator"
    
   
    # Check that Men contains products and each of there are avaliable:
    wait_for_element('//section[@id="products"]')
    child_elements = driver.find_elements(By.XPATH, '//div[@class="products row"]')
    children_count = len(child_elements) 
    
    assert children_count > 0, "No child elements found within product cards"
    for child in child_elements:
        assert child.is_displayed(), "Child element is not visible"      
    
    
    
    
    
    
    
  