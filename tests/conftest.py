import pytest

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser type")
    parser.addoption("--env", action="store", default="dev", help="Environment")
