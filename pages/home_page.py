from utils.selenium_wrapper import SeleniumWrapper
# from configs.configs import home_page_locators

class HomePage(SeleniumWrapper):

	def __init__(self, context):
		super().__init__(context)
		self.context = context
	def visit_home_page(self):
		self.driver.get(self.context['baseurl'])
