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

---
## Project Foto
- You can view the project photo [here](https://drive.google.com/file/d/16NlwY4c6LlZIT03l575fhe9UNs3B_iCp/view?usp=sharing).
- You can view the CI (GitHub Actions) photo [here](https://drive.google.com/file/d/17g_aE7-ORcpqNbzI8XSFPGCnUp9K5ji3/view?usp=sharing).
---
## Project Video

You can watch the project video [here](https://drive.google.com/file/d/1WYFYeKUsBqskbnGyemiqKeKtWVNvv30N/view?usp=sharing).
