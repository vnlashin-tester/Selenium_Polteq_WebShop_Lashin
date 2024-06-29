#  Import:
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_complex(driver, login_fixture):
    
    # Check that banner and carousel are displayed: 
    main_logo_in_the_header = driver.find_element(By.XPATH, '//div[@id="_desktop_logo"]')
    main_logo_in_the_header.click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@id="carousel"]')))
    assert driver.find_element(By.XPATH, '//section[@id="content"]/a[@class="banner"]'), "Error: Discount banner is not avaliable"    
    assert driver.find_element(By.XPATH, '//div[@id="carousel"]'), "Error: Carousel is not avaliable"
    
    # Mouse over element drop down menu clothes:
    drop_down_menu_clothes = driver.find_element(By.XPATH, '//li[@id="category-3"]/a[@class="dropdown-item"]')
    action = ActionChains(driver)
    action.move_to_element(drop_down_menu_clothes)
    action.perform()
    
    # Choise Clothes > Men submenu:
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//li[@id="category-4"]/a[contains(text(), "Men")]')))
    submenu_drop_down_menu_man = driver.find_element(By.XPATH, '//li[@id="category-4"]/a[contains(text(), "Men")]')    
    submenu_drop_down_menu_man.click()
    
    # Choise first item from catalog: 
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//h1[contains(text(), "Men")]')))
    article_from_men_clothes = driver.find_element(By.XPATH, '//article[@data-id-product="1"]') 
    article_from_men_clothes.click()
    
    # Add to cart:
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//button[@data-button-action="add-to-cart"]')))
    button_add_to_cart = driver.find_element(By.XPATH, '//button[@data-button-action="add-to-cart"]')      
    button_add_to_cart.click()
    
    # Work with cart and order:
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//h4[@id="myModalLabel"]')))
    
    button_proceed_to_checkout = driver.find_element(By.XPATH, '//a[@class="btn btn-primary"]')
    button_proceed_to_checkout.click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//h1[contains(text(), "Shopping Cart")]')))
    
    button_proceed_to_checkout_2 = driver.find_element(By.XPATH, '//a[contains(text(),"Proceed to checkout")]')  
    button_proceed_to_checkout_2.click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//section[@id="checkout-personal-information-step"]')))
    
    button_confirm_adress_continue = driver.find_element(By.XPATH, '//button[@name="confirm-addresses"]')  
    button_confirm_adress_continue.click()
    
    # Check that 1 item in the cart:
    radio_with_first_position = driver.find_element(By.XPATH, '//span/input[@id="delivery_option_1"]')
    actual_value = radio_with_first_position.get_attribute("value")
    assert actual_value == "1,", f"Error: Expected attribute value to be '1,', but it was '{actual_value}'"
    
    button_continue_in_cart = driver.find_element(By.XPATH, '//button[@name="confirmDeliveryOption"]')
    button_continue_in_cart.click()
    
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//form[@id="conditions-to-approve"]/ul/li[1]')))
    check_i_agree_in_cart = driver.find_element(By.XPATH, '//form[@id="conditions-to-approve"]/ul/li[1]')  
    check_i_agree_in_cart.click()
 