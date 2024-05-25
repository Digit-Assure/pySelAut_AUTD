# PySelAut_AUTD

## Python Selenium Automation "Always Up To Date"!

### Features
- Page Object Model (check pages directory)
- Centralized locators (locators/locators.py)
- Passing env variables from command line (like browser=chrome, env=QA etc)
- headless & headed execution (--headless=true|false )
- support for chrome & firefox
- 
### Pre-requisite
- Python 3 (built on 3.12)

### Installation 
`pip install -r requirements.txt`

### How to run
```
pytest -srP --browser=chrome --headless=true --env=QA --login=standard_user --secret=secret_sauce tests/example_tests/example_test.py
```
#### To run with allure report
```
pytest -srP --alluredir=allure-report --browser=chrome --headless=true --env=QA --login=standard_user --secret=secret_sauce tests/example_tests/example_test.py
```
