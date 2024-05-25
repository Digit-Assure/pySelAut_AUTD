import pytest

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser type")
    parser.addoption("--env", action="store", default="dev", help="Environment")
    parser.addoption("--login", action="store", default="dev", help="User name")
    parser.addoption("--secret", action="store", default="dev", help="Password")
    parser.addoption("--headless", action="store", default="dev", help="y or n")
