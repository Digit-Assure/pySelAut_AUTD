from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from utils.base_driver import Browser

class SeleniumWrapper(Browser):

    def __init__(self):
        super().__init__()

    # to navigate to any url
    def visit(self, url):
        self.driver.get(url)

    # using css selector as default locator strategy
    def click(self, selector, xpath=True):
        if xpath: self.driver.find_element(By.XPATH, selector).click()
        else: self.driver.find_element(By.CSS_SELECTOR, selector).click()