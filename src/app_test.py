"""
Tests for main.py for CI
"""

import unittest
import main as tested_app

class FlaskAppTests(unittest.TestCase):
    """
    List of test cases
    """

    def setUp(self):
        tested_app.app.config['TESTING'] = True
        self.app = tested_app.app.test_client()

    def test_get_hello_endpoint(self):
        """
        Tests a GET request to see if web server is functioning
        """
        response = self.app.get('/')
        print(self.assertEqual(response.data, b'Hello World!!!'))
        print(self.assertEqual(response.status_code, 200))

if __name__ == '__main__':
    unittest.main()
