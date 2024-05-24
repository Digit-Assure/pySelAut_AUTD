from selenium import webdriver
from configs.configs import browser

class Browser():

	def __init__(self):
		driver = None

		if browser == 'chrome':
			driver = webdriver.Chrome()

		elif browser == 'firefox':
			driver = webdriver.Firefox()

		self.driver = driver
		self.driver.maximize_window()
	
	def close_browser(self):
		self.driver.quit()
