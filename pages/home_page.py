from utils.selenium_wrapper import SeleniumWrapper
from locators.locators import *

class HomePage(SeleniumWrapper):

	def __init__(self, context):
		super().__init__(context)
		self.context = context

	def visit_home_page(self):
		self.driver.get(self.context['baseurl'])

	def verify_home_page(self):
		self.visit_home_page()
		self.assert_text(home_page['login_logo_text'], 'Swag Labs')
		self.input_text(home_page['username_field'], self.context['login'])
		self.input_text(home_page['password_field'], self.context['secret'])
		self.click(home_page['login_btn'])
		self.assert_text(home_page['home_page_main_heading_txt'], 'Swag Labs')
