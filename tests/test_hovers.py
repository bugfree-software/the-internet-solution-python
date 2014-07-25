from . import TheInternetTestCase
from helium.api import Image, find_all, hover, Text

class FileUploadTest(TheInternetTestCase):
	def get_page(self):
		return "http://the-internet.herokuapp.com/hovers"
	def test_hover_images(self):
		images = find_all(
			Image(below="Hover over the image for additional information")
		)
		# sort the images - from left to right
		images.sort(key=lambda image: image.x)
		for index in range(0, len(images)):
			self.assertFalse(Text("name: user%d" % (index + 1)).exists())
			hover(images[index])
			self.assertTrue(Text("name: user%d" % (index + 1)).exists())