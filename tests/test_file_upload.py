from . import TheInternetTestCase
from helium.api import attach_file, click, Text

class FileUploadTest(TheInternetTestCase):
	def get_page(self):
		return "http://the-internet.herokuapp.com/upload"
	def test_upload_file(self):
		attach_file(__file__, "Choose a file here on your system that you would like to upload!")
		click("Upload")
		self.assertTrue(Text("File Uploaded!").exists())