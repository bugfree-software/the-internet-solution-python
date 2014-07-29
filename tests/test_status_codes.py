from . import TheInternetTestCase
from helium.api import Link, find_all
from httplib import HTTPConnection
from urlparse import urlparse

class StatusCodesTest(TheInternetTestCase):
	def get_page(self):
		return "http://the-internet.herokuapp.com/status_codes"
	def test_status_code_200(self):
		self._test_status_code(200)
	def test_status_code_301(self):
		self._test_status_code(301)
	def test_status_code_404(self):
		self._test_status_code(404)
	def test_status_code_500(self):
		self._test_status_code(500)
	def _test_status_code(self, status_code):
		self.assertEqual(
			self._get_status_code(
				"http://the-internet.herokuapp.com/" + Link(str(status_code)).href
			), status_code
		)
	def _get_status_code(self, url):
		parsed_url = urlparse(url)
		try:
			conn = HTTPConnection(parsed_url.netloc)
			conn.request("HEAD", parsed_url.path)
			return conn.getresponse().status
		except StandardError:
			return None