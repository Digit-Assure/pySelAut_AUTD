import pytest
import logging

logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)
logger.info("Testing logging")

# Global setup and teardown (session scope)
@pytest.fixture(scope="session")
def global_setup(request):
    browser_type = request.config.getoption("--browser")
    env = request.config.getoption("--env")
    logger.info(f"\nGlobal Setup: Browser Type - {browser_type}, Environment - {env}")
    yield
    logger.info("Global Teardown")

# Test-specific setup and teardown (function scope)
@pytest.fixture()
def test_setup_and_teardown_1():
    logger.info("\nTest Setup1")
    yield
    logger.info("Test Teardown1")

@pytest.fixture()
def test_setup_and_teardown_2():
    logger.info("\nTest Setup2")
    yield
    logger.info("Test Teardown2")

def test_example_1(global_setup, test_setup_and_teardown_1):
    logger.info("Executing test_example_1")
    assert True

def test_example_2(global_setup, test_setup_and_teardown_2):
    logger.info("Executing test_example_2")
    assert True
