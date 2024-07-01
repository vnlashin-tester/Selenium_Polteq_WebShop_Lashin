
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.run(order=2)
def test_complex(driver, only_login_fixture):
    """ The complex test cheks:
    1. Login
    2. Avaliable discount banner and carousel on the main page
    3. Check the drop-down menu
    4. Go to the Clothes > Man page and choise the item
    5. Add item to the cart
    6. Order the item (fullfill the fields of order form)
    7. I used fixtures
    8. I created a wait_for_element function
    
    In this version I refactored my code and I craeted new function
    wait_for_element(xpath) and I made tests with this function. I inproved readabillity
    and reduced duplicate code.
    And now each step waits for necessary elements to be visible before proceeding.
 
    """
    
    def wait_for_element(xpath):
        return WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))

    # Check that banner and carousel are displayed
    main_logo_in_the_header = wait_for_element('//div[@id="_desktop_logo"]')
    main_logo_in_the_header.click()
    wait_for_element('//div[@id="carousel"]')
    assert driver.find_element(By.XPATH, '//section[@id="content"]/a[@class="banner"]'), "Error: Discount banner is not available"
    assert driver.find_element(By.XPATH, '//div[@id="carousel"]'), "Error: Carousel is not available"
    
    # Mouse over element drop down menu clothes
    drop_down_menu_clothes = wait_for_element('//li[@id="category-3"]/a[@class="dropdown-item"]')
    ActionChains(driver).move_to_element(drop_down_menu_clothes).perform()
    
    # Choose Clothes > Men submenu
    wait_for_element('//li[@id="category-4"]/a[contains(text(), "Men")]').click()
    
    # Choose first item from catalog
    wait_for_element('//h1[contains(text(), "Men")]')
    article_from_men_clothes = wait_for_element('//article[@data-id-product="1"]')
    article_from_men_clothes.click()
    
    # Add to cart
    wait_for_element('//button[@data-button-action="add-to-cart"]').click()
    
    # Work with cart and order
    wait_for_element('//h4[@id="myModalLabel"]')
    
    driver.find_element(By.XPATH, '//a[@class="btn btn-primary"]').click()
    wait_for_element('//h1[contains(text(), "Shopping Cart")]')
    
    driver.find_element(By.XPATH, '//a[contains(text(),"Proceed to checkout")]').click()
    wait_for_element('//section[@id="checkout-personal-information-step"]')
    
    driver.find_element(By.XPATH, '//button[@name="confirm-addresses"]').click()
    
    # Check that 1 item in the cart
    radio_with_first_position = driver.find_element(By.XPATH, '//span/input[@id="delivery_option_1"]')
    actual_value = radio_with_first_position.get_attribute("value")
    assert actual_value == "1,", f"Error: Expected attribute value to be '1,', but it was '{actual_value}'"
    
    driver.find_element(By.XPATH, '//button[@name="confirmDeliveryOption"]').click()
    
    wait_for_element('//form[@id="conditions-to-approve"]/ul/li[1]').click()
