from selenium import webdriver
from selenium.webdriver.firefox.options import Options as firefox_options
from selenium.webdriver.chrome.options import Options as chrome_options

class BaseDriver():

	def __init__(self, context):

		if context['browser'] == 'chrome':
			options = chrome_options()
			if context['headless'] == 'true': options.add_argument("--headless")
			self.driver = webdriver.Chrome(options)

		elif context['browser'] == 'firefox':
			options = firefox_options()
			if context['headless'] == 'true': options.headless = True
			self.driver = webdriver.Firefox(options)

		self.driver.maximize_window()
		self.driver.implicitly_wait(30)
	
	def close_browser(self):
		self.driver.quit()
