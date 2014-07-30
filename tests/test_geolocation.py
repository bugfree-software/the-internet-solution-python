from . import TheInternetTestCase
from helium.api import click, get_driver, S

class GeolocationTest(TheInternetTestCase):
	def get_page(self):
		return "http://the-internet.herokuapp.com/geolocation"
	def test_fake_geolocation(self):
		get_driver().execute_script(
			'window.navigator.geolocation.getCurrentPosition = '
				'function(success){ '
					'var position = {"coords" : { '
						'"latitude": "1", '
						'"longitude": "2"'
						'}'
				'}; '
			'success(position);}'
		)
		click('Where am I?')
		latitude = S("#lat-value").web_element.text
		self.assertEqual(latitude, u"1")
		longitude = S("#long-value").web_element.text
		self.assertEqual(longitude, u"2")