# Playwright Test Automation Framework - SauceDemo

A complete end-to-end test automation framework built with Playwright and Python, implementing the Page Object Model (POM) design pattern.

## Project Overview

This project demonstrates professional test automation practices for the SauceDemo e-commerce application. The framework includes 26 comprehensive UI tests covering critical user workflows including authentication, product browsing, shopping cart operations, and checkout processes.

## 🛠Technologies Used

- **Playwright** - Modern web automation framework
- **Python 3.14** - Programming language
- **pytest** - Testing framework
- **Page Object Model** - Design pattern for maintainable test code

## Project Structure
```
playwright-saucedemo-automation/
├── pages/
│   ├── base_page.py          # Base class with common methods
│   ├── login_page.py          # Login page objects and methods
│   ├── products_page.py       # Products page objects and methods
│   ├── cart_page.py           # Shopping cart page objects and methods
│   └── checkout_page.py       # Checkout page objects and methods
├── tests/
│   ├── test_login.py          # Login functionality tests (7 tests)
│   ├── test_products.py       # Product page tests (7 tests)
│   ├── test_cart.py           # Shopping cart tests (7 tests)
│   └── test_checkout.py       # Checkout process tests (5 tests)
├── pytest.ini                 # Pytest configuration
└── README.md
```

## Key Features

- **Page Object Model**: Clean separation between test code and page elements
- **Reusable Components**: BasePage class with common functionality
- **Comprehensive Coverage**: 26 tests covering main user journeys
- **Maintainable**: Easy to update when UI changes
- **Cross-browser Ready**: Configured for Chromium (easily extensible)

## Test Coverage

| Module | Tests | Description |
|--------|-------|-------------|
| Login | 7 | Authentication, validation, error handling |
| Products | 7 | Product display, details, filtering |
| Cart | 7 | Add/remove items, badge updates |
| Checkout | 5 | Form validation, order completion |
| **Total** | **26** | **Complete e-commerce workflow** |

## Getting Started

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### Installation

1. Clone the repository
```bash
git clone https://github.com/RoyaValiyeva/playwright-saucedemo-automation.git
cd playwright-saucedemo-automation
```

2. Create virtual environment
```bash
python -m venv .venv
```

3. Activate virtual environment
```bash
# Windows
.venv\Scripts\activate.bat

# Mac/Linux
source .venv/bin/activate
```

4. Install dependencies
```bash
pip install pytest pytest-playwright playwright pytest-base-url
```

5. Install Playwright browsers
```bash
playwright install
```

## Running Tests

### Run all tests
```bash
pytest tests/ -v
```

### Run specific test file
```bash
pytest tests/test_login.py -v
```

### Run tests in quiet mode
```bash
pytest tests/ -q
```

### Run with headed browser (see tests execute)
```bash
pytest tests/ -v --headed
```

## Sample Test Execution

All 26 tests pass successfully:
```
tests/test_login.py::test_login_page_loads PASSED
tests/test_login.py::test_successful_login_with_standard_user PASSED
tests/test_products.py::test_products_page_displays_items PASSED
tests/test_cart.py::test_add_to_cart_updates_badge PASSED
tests/test_checkout.py::test_complete_checkout_flow PASSED
...
========================= 26 passed in 45.23s =========================
```

## Design Patterns

### Page Object Model (POM)

Each page in the application has a corresponding page class that encapsulates:
- **Locators**: Element identifiers stored in one place
- **Actions**: Methods to interact with the page
- **Verifications**: Methods to assert page state

**Example:**
```python
class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_field = page.locator("[data-test='username']")
        self.password_field = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")
    
    def login(self, username, password):
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()
```

## Configuration

Key configurations in `pytest.ini`:
- Base URL: https://www.saucedemo.com
- Test file pattern: `test_*.py`
- Verbose output enabled

## Future Enhancements

- [ ] Cross-browser testing (Firefox, Safari)
- [ ] Mobile responsive testing
- [ ] CI/CD pipeline integration (GitHub Actions)
- [ ] HTML test reports
- [ ] Screenshot on failure
- [ ] Video recording

## Author

**Roya Valiyeva**
- GitHub: [@RoyaValiyeva](https://github.com/RoyaValiyeva)

## License

This project is created for educational and portfolio purposes.

## Acknowledgments

- SauceDemo for providing the test application
- Playwright team for the excellent automation framework