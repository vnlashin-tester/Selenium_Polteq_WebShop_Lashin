import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.run(order=7)
def test_clothes_and_submenus(driver, login_fixture, logout_fixture):
    """ 
    This test checks drop-down main menu.
    Clothes menu - avaliable
    1. Test submenu Clothes > Men: check avaliable, click menu-item, check that all of
    product-cards are avaliable.
    2. Test submenu Clothes > Women: check avaliable, click menu-item, check that all of
    product-cards are avaliable.
    3. Test submenus Clothes with Men and Women items: check avaliable, click menu-item, check that all of
    product-cards are avaliable.
    4. Test submenu Accessories > Stationery: check avaliable, click menu-item, check that all of
    product-cards are avaliable.
    5. Test submenu Accessories > Home accessories: check avaliable, click menu-item, check that all of
    product-cards are avaliable.
    6. Test Accessories with Stationery and Home Accessories: check avaliable, click menu-item, check that all of
    product-cards are avaliable.
    7. Test Art menu: check avaliable, click menu-item, check that all of
    product-cards are avaliable.    
    
    """
    #  1. Clothes > Men:
    
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
    
    
    # 2. Clothes > Women:
    
    main_logo_in_the_header = wait_for_element('//div[@id="_desktop_logo"]')
    main_logo_in_the_header.click()
    wait_for_element('//input[@type="text"]')
    
    # Mouse over element drop down menu clothes
    drop_down_menu_clothes = wait_for_element('//li[@id="category-3"]/a[@class="dropdown-item"]')
    ActionChains(driver).move_to_element(drop_down_menu_clothes).perform()
    wait_for_element('//a[@class="dropdown-item dropdown-submenu" and contains(text(), "Women")]')

    # Check that Women section is visible and has content:
    submenu_drop_down_menu_clothes_women = driver.find_element(By.XPATH, '//a[@class="dropdown-item dropdown-submenu" and contains(text(), "Women")]')
    submenu_drop_down_menu_clothes_women.click()
    wait_for_element('//h1[contains(text(), "Women")]')
    time.sleep(3)
    search_field = driver.find_elements(By.XPATH, '//input[@type="text"]')
    filter_by_block = driver.find_elements(By.XPATH, '//p[contains(text(), "Filter By")]')    
    assert len(search_field) > 0, "Error: No search_field found with specified locator"
    assert len(filter_by_block) > 0, "Error: No filter_block found with specified locator"
    
   
    # Check that Women contains products and each of there are avaliable:
    wait_for_element('//section[@id="products"]')
    child_elements = driver.find_elements(By.XPATH, '//div[@class="products row"]')
    children_count = len(child_elements) 
    
    assert children_count > 0, "No child elements found within product cards"
    for child in child_elements:
        assert child.is_displayed(), "Child element is not visible"      
    
    
    #  3. Test menu Clothes (Men+Women items)
    
    main_logo_in_the_header = wait_for_element('//div[@id="_desktop_logo"]')
    main_logo_in_the_header.click()
    wait_for_element('//input[@type="text"]')
    
    wait_for_element('//li[@ id="category-3" ]/a[@class="dropdown-item"]').click()
    
    clothes_menu_men = driver.find_elements(By.XPATH, '//ul[@ class="category-sub-menu"]//a[contains(text(), "Men")]')
    assert len(clothes_menu_men) > 0, "Error: No men submenu found with specified locator"
    clothes_menu_women = driver.find_elements(By.XPATH, '//ul[@ class="category-sub-menu"]//a[contains(text(), "Women")]')  
    assert len(clothes_menu_women) > 0, "Error: No womwn submenu found with specified locator"
    search_field = driver.find_elements(By.XPATH, '//input[@type="text"]')
    filter_by_block = driver.find_elements(By.XPATH, '//p[contains(text(), "Filter By")]')    
    assert len(search_field) > 0, "Error: No search_field found with specified locator"
    assert len(filter_by_block) > 0, "Error: No filter_block found with specified locator"

    # Check that Stationary contains products and each of there are avaliable:
    wait_for_element('//section[@id="products"]')
    child_elements = driver.find_elements(By.XPATH, '//div[@class="products row"]')
    children_count = len(child_elements) 
    
    assert children_count > 0, "No child elements found within product cards"
    for child in child_elements:
        assert child.is_displayed(), "Child element is not visible"   
    
    
    # 4. Accessories > Stationery
    
    main_logo_in_the_header = wait_for_element('//div[@id="_desktop_logo"]')
    main_logo_in_the_header.click()
    wait_for_element('//input[@type="text"]')
    
    # Mouse over element drop down menu Accessories
    drop_down_menu_accessories = wait_for_element('//li[@id="category-6"]')
    ActionChains(driver).move_to_element(drop_down_menu_accessories).perform()
    wait_for_element('//a[@class="dropdown-item dropdown-submenu" and contains(text(), "Stationery")]')
    
    # Check that Sattionary section is visible and has content:
    drop_menu_items_stationery = driver.find_element(By.XPATH, '//a[@class="dropdown-item dropdown-submenu" and contains(text(), "Stationery")]')          
    drop_menu_items_stationery.click()
    wait_for_element('//h1[contains(text(), "Stationery")]')
    
    search_field = driver.find_elements(By.XPATH, '//input[@type="text"]')
    filter_by_block = driver.find_elements(By.XPATH, '//p[contains(text(), "Filter By")]')    
    assert len(search_field) > 0, "Error: No search_field found with specified locator"
    assert len(filter_by_block) > 0, "Error: No filter_block found with specified locator"
       
    # Check that Stationary contains products and each of there are avaliable:
    wait_for_element('//section[@id="products"]')
    child_elements = driver.find_elements(By.XPATH, '//div[@class="products row"]')
    children_count = len(child_elements) 
    
    assert children_count > 0, "No child elements found within product cards"
    for child in child_elements:
        assert child.is_displayed(), "Child element is not visible"    
    
    # 5. Accessories > Home Accessories
    
    main_logo_in_the_header = wait_for_element('//div[@id="_desktop_logo"]')
    main_logo_in_the_header.click()
    wait_for_element('//input[@type="text"]')
    
    # Mouse over element drop down menu Accessories
    drop_down_menu_accessories = wait_for_element('//li[@id="category-6"]')
    ActionChains(driver).move_to_element(drop_down_menu_accessories).perform()
    wait_for_element('//a[@class="dropdown-item dropdown-submenu" and contains(text(), "Stationery")]')
    
    # Check that Sattionary section is visible and has content:
    drop_menu_items_home_accessories = driver.find_element(By.XPATH, '//a[@class="dropdown-item dropdown-submenu" and contains(text(), "Home Accessories")]')          
    drop_menu_items_home_accessories.click()
    wait_for_element('//h1[contains(text(), "Home Accessories")]')
   
    search_field = driver.find_elements(By.XPATH, '//input[@type="text"]')
    filter_by_block = driver.find_elements(By.XPATH, '//p[contains(text(), "Filter By")]')    
    assert len(search_field) > 0, "Error: No search_field found with specified locator"
    assert len(filter_by_block) > 0, "Error: No filter_block found with specified locator"
       
    # Check that Stationary contains products and each of there are avaliable:
    wait_for_element('//section[@id="products"]')
    child_elements = driver.find_elements(By.XPATH, '//div[@class="products row"]')
    children_count = len(child_elements) 
    
    assert children_count > 0, "No child elements found within product cards"
    for child in child_elements:
        assert child.is_displayed(), "Child element is not visible"   

    # 6. Test Accessories (Stationary+Home Accessories)
    
    main_logo_in_the_header = wait_for_element('//div[@id="_desktop_logo"]')
    main_logo_in_the_header.click()
    wait_for_element('//input[@type="text"]')
    
    wait_for_element('//li[@id="category-6"]').click()
  
    accessories_menu_stationery = driver.find_elements(By.XPATH, '//ul[@ class="category-sub-menu"]//a[contains(text(), "Stationery")]')
    assert len(accessories_menu_stationery) > 0, "Error: No men submenu found with specified locator"
    accessories_menu_home_accessories = driver.find_elements(By.XPATH, '//ul[@ class="category-sub-menu"]//a[contains(text(), "Home Accessories")]')  
    assert len(accessories_menu_home_accessories) > 0, "Error: No womwn submenu found with specified locator"
    search_field = driver.find_elements(By.XPATH, '//input[@type="text"]')
    filter_by_block = driver.find_elements(By.XPATH, '//p[contains(text(), "Filter By")]')    
    assert len(search_field) > 0, "Error: No search_field found with specified locator"
    assert len(filter_by_block) > 0, "Error: No filter_block found with specified locator"
    
    # Check that Stationary contains products and each of there are avaliable:
    wait_for_element('//section[@id="products"]')
    child_elements = driver.find_elements(By.XPATH, '//div[@class="products row"]')
    children_count = len(child_elements) 
    
    assert children_count > 0, "No child elements found within product cards"
    for child in child_elements:
        assert child.is_displayed(), "Child element is not visible"   
   
   
    # 7. Menu "Art"
    
    main_logo_in_the_header = wait_for_element('//div[@id="_desktop_logo"]')
    main_logo_in_the_header.click()
    wait_for_element('//input[@type="text"]')
    
    menu_art = driver.find_element(By.XPATH, '//li[@id="category-9"]')    
    menu_art.click()
    wait_for_element('//h1[contains(text(), "Art")]')
  
    
    search_field = driver.find_elements(By.XPATH, '//input[@type="text"]')
    filter_by_block = driver.find_elements(By.XPATH, '//p[contains(text(), "Filter By")]')    
    assert len(search_field) > 0, "Error: No search_field found with specified locator"
    assert len(filter_by_block) > 0, "Error: No filter_block found with specified locator"
    
    # Check that Stationary contains products and each of there are avaliable:
    wait_for_element('//section[@id="products"]')
    child_elements = driver.find_elements(By.XPATH, '//div[@class="products row"]')
    children_count = len(child_elements) 
    
    assert children_count > 0, "No child elements found within product cards"
    for child in child_elements:
        assert child.is_displayed(), "Child element is not visible"   
   