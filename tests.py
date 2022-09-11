import unittest
from main import app

class Basic_Tests(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_login(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)
    
    def test_sign_up(self):
        response = self.app.get('/sign_up')
        self.assertEqual(response.status_code, 200)
    
    def home_when_logged_out(self):
        response = self.app.get('/')
        self.assertNotEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()