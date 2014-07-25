from . import TheInternetTestCase
from helium.api import Text, write, press, ENTER, click

class BasicAuthTest(TheInternetTestCase):
	def get_page(self):
		return "http://the-internet.herokuapp.com/login"
	def test_valid_credentials(self):
		self._login("tomsmith", "SuperSecretPassword!")
		self.assertTrue(Text("Secure Area").exists())
		self._logout()
	def test_no_credentials(self):
		click("Login")
		self.assertTrue(Text("Your username is invalid!").exists())
	def test_invalid_password(self):
		self._login("tomsmith", "INVALID_PASSWORD")
		self.assertTrue(Text("Your password is invalid!").exists())
	def _login(self, username, password):
		write(username, into="Username")
		write(password, into="Password")
		press(ENTER)
	def _logout(self):
		click("Logout")
		self.assertTrue(Text("You logged out of the secure area!").exists())