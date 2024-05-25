# PySelAut_AUTD

## Python Selenium Automation "Always Up To Date"!

### Features
- Page Object Model
- Centralized selectors
- Passing env variables from command line
- headless & headed execution

### Pre-requisite
- Python 3 (built on 3.12)

### Installation 
`pip install -r requirements.txt`

### How to run
`pytest -srP --browser=chrome --headless=true --env=QA --login=standard_user --secret=secret_sauce tests/example_tests/example_test.py`