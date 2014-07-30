from . import TheInternetTestCase
from helium.api import start_chrome, S, get_driver, set_driver, write, click, \
	Text, Link, kill_browser, wait_until

class ForgotPasswordTest(TheInternetTestCase):
	def get_page(self):
		return "http://the-internet.herokuapp.com/forgot_password"
	def test_retrieve_password(self):
		email_address = self._get_temporary_email_address()
		write(email_address, into="E-mail")
		click("Retrieve Password")
		self.assertTrue(Text("Your e-mail's been sent!").exists())
		set_driver(self.emailbox_driver)
		wait_until(
			self._refresh_and_check_if_exists,
			timeout_secs=60, interval_secs=1
		)
		self.assertTrue(Text("no-reply@the-internet.herokuapp.com").exists())
		kill_browser()
		set_driver(self.test_case_driver)
	def _get_temporary_email_address(self):
		self.test_case_driver = get_driver()
		start_chrome("http://temp-mail.org/")
		self.emailbox_driver = get_driver()
		email_address = S("#email").web_element.text
		set_driver(self.test_case_driver)
		return email_address
	def _refresh_and_check_if_exists(self):
		click("Refresh")
		return Link("Forgot Password from the").exists()