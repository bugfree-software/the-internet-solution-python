from . import TheInternetTestCase
from helium.api import drag, Text

class DragAndDropTest(TheInternetTestCase):
	def get_page(self):
		return "http://the-internet.herokuapp.com/drag_and_drop"
	def test_drag_and_drop(self):
		self.assertTrue(Text("A", to_left_of=Text("B")).exists())
		self.assertFalse(Text("A", to_right_of=Text("B")).exists())
		drag("A", "B")
		self.assertFalse(Text("A", to_left_of=Text("B")).exists())
		self.assertTrue(Text("A", to_right_of=Text("B")).exists())