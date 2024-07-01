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
    
    # Click the logo
    main_logo_in_the_header = wait_for_element('//div[@id="_desktop_logo"]')
    main_logo_in_the_header.click()
    wait_for_element('//h2[contains(text(), "Popular Products")]')
    
    # Choise third element of products
    third_element_of_popular_products = driver.find_element(By.XPATH, '//div[@itemprop="itemListElement"][3]')
    third_element_of_popular_products.click()    
    wait_for_element('//div[@class="product-information"]')
        
    # Add good to cart
    button_add_to_cart = driver.find_element(By.XPATH, '//button[@data-button-action="add-to-cart"]')
    button_add_to_cart.click()
    wait_for_element('//h4[@ id="myModalLabel"]')
    
    button_proceed_to_checkout = driver.find_element(By.XPATH, '//*[contains(text(), "Proceed to checkout")]')
    button_proceed_to_checkout.click()
    wait_for_element('//h1[contains(text(), "Shopping Cart")]')
    
    button_proceed_to_checkout = driver.find_element(By.XPATH, '//*[contains(text(), "Proceed to checkout")]')
    button_proceed_to_checkout.click()
    wait_for_element('//button[@name="confirm-addresses"]')
    
    button_confirm_address = driver.find_element(By.XPATH, '//button[@name="confirm-addresses"]') 
    button_confirm_address.click()
    wait_for_element('//section[@ id="checkout-delivery-step"]')
    
    button_confirm_delivery_option = driver.find_element(By.XPATH, '//button[@name="confirmDeliveryOption"]')
    button_confirm_delivery_option.click()
    wait_for_element('//span[@class="custom-checkbox"]')
    
    check_box_agree = driver.find_element(By.XPATH, '//span[@class="custom-checkbox"]')
    check_box_agree.click()
    
    
    # Return to the main page
    logo_on_the_order_page = driver.find_element(By.XPATH, '//div[@id="_desktop_logo"]/a/img')    
    logo_on_the_order_page.click()
    wait_for_element('//h2[contains(text(), "Popular Products")]')
    
    