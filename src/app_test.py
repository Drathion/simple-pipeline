import unittest
import main as tested_app
#import json


class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        tested_app.app.config['TESTING'] = True
        self.app = tested_app.app.test_client()

    def test_get_hello_endpoint(self):
        r = self.app.get('/')
        self.assertEqual(r.data, b'Hello World!!!')
        self.assertEqual(r.status_code, 200)

    """ 
    Test examples from ozada/flask-app-github-actions -- thank you!

    # Example test case to test a POST to '/' endpoint
    def test_post_hello_endpoint(self):
        r = self.app.post('/')
        self.assertEqual(r.status_code, 405)

    # Example test case to GET to '/api' endpoint
    def test_get_api_endpoint(self):
        r = self.app.get('/api')
        self.assertEqual(r.json, {'status': 'test'})

    # Example test case to POST to '/api' endpoint with correct expected payload
    def test_correct_post_api_endpoint(self):
        r = self.app.post('/api',
                          content_type='application/json',
                          data=json.dumps({'name': 'Den', 'age': 100}))
        self.assertEqual(r.json, {'status': 'OK'})
        self.assertEqual(r.status_code, 200)

        r = self.app.post('/api',
                          content_type='application/json',
                          data=json.dumps({'name': 'Den'}))
        self.assertEqual(r.json, {'status': 'OK'})
        self.assertEqual(r.status_code, 200)

    # Example test case to POST with incorrect formatted payload (not dictionary)
    def test_not_dict_post_api_endpoint(self):
        r = self.app.post('/api',
                          content_type='application/json',
                          data=json.dumps([{'name': 'Den'}]))
        self.assertEqual(r.json, {'status': 'bad input'})
        self.assertEqual(r.status_code, 400)

    # Example test case to POST with incorrect data (no name, only age)
    def test_no_name_post_api_endpoint(self):
        r = self.app.post('/api',
                          content_type='application/json',
                          data=json.dumps({'age': 100}))
        self.assertEqual(r.json, {'status': 'bad input'})
        self.assertEqual(r.status_code, 400)

    # Exmaple test case to POST with incorrect data (age as a string, not int)
    def test_bad_age_post_api_endpoint(self):
        r = self.app.post('/api',
                          content_type='application/json',
                          data=json.dumps({'name': 'Den', 'age': '100'}))
        self.assertEqual(r.json, {'status': 'bad input'})
        self.assertEqual(r.status_code, 400)
    """

if __name__ == '__main__':
    unittest.main()