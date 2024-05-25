import pytest
import logging
from utils.get_env_details import get_env_details
from pages.home_page import HomePage
from time import sleep

logging.getLogger().setLevel(logging.INFO)
logger = logging.getLogger(__name__)

'''This is a boiler place test script, we can use this script to replicate other test script files'''
# Global setup and teardown (session scope)
@pytest.fixture(scope="session")
def global_setup(request):

    logger.info("Global Setup section")
    '''context will contain all env variables & env specific data stored in configs/env_data.py'''
    # import pdb;pdb.set_trace()
    context = get_env_details(request)

    '''create an object of HomePage class & add it in context so that it can be shared within test cases'''
    context['homepage'] = HomePage(context)

    '''now context contains, env data plus class objects'''
    yield context

    logger.info("Global Teardown section")


# Test-specific setup and teardown (function scope)
@pytest.fixture()
def test_setup():
    logger.info("\nTest Setup section")
    yield
    logger.info("\nTest Teardown section")

def test_example_2(global_setup, test_setup):
    logger.info("Executing test_example_2")

    homepage = global_setup['homepage']
    context = global_setup

    homepage.visit_home_page()

    # homepage_heading = homepage.get_text('.login_logo')
    homepage.assert_text('.login_logo', 'Swag Labs')

    homepage.input_text('#user-name', context['login'])
    homepage.input_text('#password', context['secret'])
    homepage.click('#login-button')




    sleep(5)
    assert True
