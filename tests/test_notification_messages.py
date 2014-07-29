from . import TheInternetTestCase
from helium.api import Text, click

class NotificationMessagesTest(TheInternetTestCase):
	def get_page(self):
		return "http://the-internet.herokuapp.com/notification_message_rendered"
	def test_load_new_message(self):
		success = False
		while not success:
			click("Click here")
			failure = Text("Action unsuccesful, please try again").exists()
			success = Text("Action successful").exists()
			self.assertTrue(failure or success)

