import unittest
from app import app  # Import your Flask app

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        """Set up the Flask test client before each test."""
        self.app = app.test_client()  # Create a test client
        self.app.testing = True  # Enable testing mode

    def test_home_page(self):
        """Test the home route."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)  # Check for a successful response
        self.assertIn(b'Devops lifecycle automation', response.data)  # Check the presence of the heading
        self.assertIn(b'Welcome to my awesome Flask application running in Docker.', response.data)  # Check the welcome message
        self.assertIn(b'Feel free to explore!', response.data)  # Check the additional message

    def test_home_page_content_type(self):
        """Test the content type of the home page."""
        response = self.app.get('/')
        self.assertEqual(response.content_type, 'text/html; charset=utf-8')  # Ensure the content type is correct

if __name__ == '__main__':
    unittest.main()
