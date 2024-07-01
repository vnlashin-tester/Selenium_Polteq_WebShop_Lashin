import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.run(order=7)
def test_product_card_short_way(driver, login_fixture, logout_fixture):
    """ 
    This test checks the product card. Quick way (pop-up "quick view").
    We compare two names of items (from preview and from opened product card)
    """
    
    def wait_for_element(xpath):
        return WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    
    # Click the logo
    main_logo_in_the_header = wait_for_element('//div[@id="_desktop_logo"]')
    main_logo_in_the_header.click()
    wait_for_element('//h2[contains(text(), "Popular Products")]')
    
    # Mouse over first product
    first_items_of_popular_products = wait_for_element('//div[@class="products row"]/div [1]')
    ActionChains(driver).move_to_element(first_items_of_popular_products).perform()
    
    # For comparing futher texts (create a variable)
    element_text1 = wait_for_element('//div[@class="products row"]/div [1]//h3/a').text
    
    # Pop-up quick view and open the item's card
    wait_for_element('//a[@class="quick-view"]').click()
    # Item's card
    wait_for_element('//h1[@class="h1"]')
    
    # Compare two texts from priview and from item's card (Case Insensitive):
    element_text2 = wait_for_element('//h1[@class="h1"]').text
    result = element_text1.strip().lower() == element_text2.strip().lower()
    assert result, f"Texts do not match: '{element_text1}' != '{element_text2}'"

    # Close the item's card
    close_short_card_page = driver.find_element(By.XPATH, '//button[@class="close"]')   
    close_short_card_page.click()
    
     
@pytest.mark.run(order=9)
def test_product_card_normal_way(driver, login_fixture, logout_fixture):
    """ 
    This test checks the product card. Normal way (click at item).
    We compare two names of items (from preview and from opened product card)
    """
    
    def wait_for_element(xpath):
        return WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    
    # Click the logo
    main_logo_in_the_header = wait_for_element('//div[@id="_desktop_logo"]')
    main_logo_in_the_header.click()
    wait_for_element('//h2[contains(text(), "Popular Products")]')
    
    # For comparing futher texts (create a variable)
    element_text3 = wait_for_element('//div[@class="products row"]/div [3]//h3/a').text 
    
    # Third item from popular products and click
    third_items_of_popular_products = driver.find_element(By.XPATH, '//div[@class="products row"]/div [3]')    
    third_items_of_popular_products.click()
    # Wait of opend item's card
    wait_for_element('//h1[@class="h1"]')
    
    # Compare the texts from preview and from opend item's card
    element_text4 = wait_for_element('//h1[@class="h1"]').text
    # Due to the result of two strings was different (in the first word was shorter form than in the second
    # and I need CUT first 21 letters of each words ans then compare there)
    trimmed_text3 = element_text3[:21]
    trimmed_text4 = element_text4[:21]

    result2 = trimmed_text3.lower() == trimmed_text4.lower()
    assert result2, f"Trimmed texts do not match: '{trimmed_text3}' != '{trimmed_text4}'"
    
  
    
    
    