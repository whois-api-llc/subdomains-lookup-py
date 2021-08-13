import os
import unittest
from subdomainslookup import Client
from subdomainslookup import ParameterError, ApiAuthError

domain = 'bbc.com'
domain2 = 'google.com'


class TestClient(unittest.TestCase):
    """
    Final integration tests without mocks.

    Active API_KEY is required.
    """
    def setUp(self) -> None:
        self.client = Client(os.getenv('API_KEY'))

    def test_get_correct_data(self):
        response = self.client.get(domain=domain)
        self.assertGreater(
            len(response.result.records), 0, "Empty result in response")

    def test_empty_terms(self):
        with self.assertRaises(ParameterError):
            self.client.get('')

    def test_incorrect_api_key(self):
        client = Client('at_00000000000000000000000000000')
        with self.assertRaises(ApiAuthError):
            client.get(domain=domain2)

    def test_raw_data(self):
        response = self.client.get_raw(
            domain=domain, output_format=Client.XML_FORMAT)
        self.assertTrue(response.startswith('<?xml'))


if __name__ == '__main__':
    unittest.main()
