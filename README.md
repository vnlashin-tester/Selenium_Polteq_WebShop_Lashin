# Selenium Polteq WebShop Automation

## Overview
This project contains automated tests for the Polteq WebShop, utilizing Selenium WebDriver for browser automation. The main goal is to verify the functionality of the product card feature, ensuring consistency between item previews and their detailed views.

The Polteq web shop is a special website written for company employees and is used exclusively for training testing skills and writing automated tests. 

For privacy purposes, the real login/password has been removed from the code, so it will not be possible to run automatic tests.

Below, I am attaching photos and examples of performing autotests.
---
## Project Structure

- `conftest.py`: Contains fixtures for setup and teardown processes.
- `tests/`: Directory containing all test scripts.
  - `test_product_card.py`: Contains tests related to product card functionality.
  - `test_login.py`: Contains tests for login functionality.
  - `test_cart.py`: Contains tests for cart functionality.
  - `test_search_field.py`: Contains tests for the search field.
  - `test_menu_items.py`: Contains tests for menu items.
  - `test_filter_page.py`: Contains tests for filter page functionality.
  - `test_complex.py` & `test_complex2.py`: Contains more comprehensive tests combining multiple functionalities.
---
## Test Approach and Techniques

### Selenium WebDriver

- **WebDriver Initialization**: The tests utilize Selenium WebDriver for browser automation, allowing interaction with web elements as if performed by a user.
- **Explicit Waits**: WebDriverWait is used extensively to wait for elements to be visible or clickable, ensuring the tests are robust and can handle asynchronous content loading.

### Action Chains

- **Mouse Hover**: ActionChains are used to perform complex actions like hovering over an element to trigger additional UI changes (e.g., pop-up quick views).

### Assertions

- **Text Comparison**: Tests include assertions to compare text from different parts of the application, ensuring data consistency.
- **Case Insensitivity**: Text comparisons are done in a case-insensitive manner to avoid false negatives due to text case differences.

### Test Fixtures

- **Login and Logout Fixtures**: `login_fixture` and `logout_fixture` are used to handle user authentication setup and teardown, providing a clean state for each test.

## Continuous Integration (CI)

I have implemented Continuous Integration (CI) using GitHub Actions. This ensures that our tests are automatically run on every push or pull request to the `main` branch, helping us maintain code quality and catch issues early.

[photo_github_actions](https://drive.google.com/file/d/17g_aE7-ORcpqNbzI8XSFPGCnUp9K5ji3/view?usp=sharing)

## Detailed Test Descriptions

### test_product_card_short_way

This test verifies the product card functionality via the quick view pop-up.

1. **Navigate to Home Page**: Click on the logo to return to the home page.
2. **Mouse Over Product**: Hover over the first popular product to trigger the quick view option.
3. **Capture Preview Text**: Save the product name from the preview.
4. **Open Quick View**: Click the quick view link to open the product card.
5. **Compare Texts**: Compare the product name from the preview with the name in the product card.
6. **Close Product Card**: Close the product card to return to the previous state.

### test_product_card_normal_way

This test verifies the product card functionality by clicking directly on the product.

1. **Navigate to Home Page**: Click on the logo to return to the home page.
2. **Capture Preview Text**: Save the product name of the third popular product.
3. **Open Product Card**: Click the product to open its detailed view.
4. **Compare Texts**: Compare the first 21 characters of the product name from the preview with the name in the product card.
5. **Close Product Card**: Ensure the product card can be closed or navigated away from if needed.
---
## How to Run Tests

1. **Clone the Repository**:
   ```sh
   git clone <repository_url>
   cd Selenium_Polteq_WebShop_Lashin
2. **Install Dependencies**:
  pip install -r requirements.txt
3. **Run Tests**:
   pytest
---
## Project Artifacts
Artefacts can be found on Google Drive.

- <a href="https://docs.google.com/document/d/1mu7r23lQwvueH1c_ltrmVmpEzFx3lkqlwZ1kSe0A0x4/edit?usp=sharing" target="_blank">Test Plan</a>
- <a href="https://docs.google.com/spreadsheets/d/1f4Q8VN6Gufj0R72tmPBWx7tXoL7sAcTbXJKIx3ZEtRk/edit?usp=sharing" target="_blank">User Stories</a>
- <a href="https://docs.google.com/spreadsheets/d/1bLJAJp9h3iQc03_BMJ5PXBq2RVoE54kseyUYoxY_feQ/edit?usp=sharing" target="_blank">Checklists and Trace Matrix</a>
- <a href="https://vnlashin-tester.github.io/Mind_Map/markmap.html" target="_blank">Mind_Map</a> 
---
## Test Reports

I generated detailed test reports using `pytest-html` and `Allure`.

### [pytest-html](https://drive.google.com/file/d/1BhHSUf5RCV2NeKoZVlgSVAp0XJeE2rlQ/view?usp=sharing)

To generate and view the HTML report locally, run:

```sh
pytest --html=report.html --self-contained-html

---
## Project Foto
- You can view the project photo [here](https://drive.google.com/file/d/16NlwY4c6LlZIT03l575fhe9UNs3B_iCp/view?usp=sharing).
- You can view the CI (GitHub Actions) photo [here](#).
---
## Project Video

You can watch the project video [here](https://drive.google.com/file/d/1WYFYeKUsBqskbnGyemiqKeKtWVNvv30N/view?usp=sharing).
