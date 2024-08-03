import unittest
from app import app

class EmotionDetectionTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_analyze(self):
        response = self.app.post('/analyze', json={'text': 'I am very happy today!'})
        data = response.get_json()
        self.assertIn('emotions', data)
        self.assertIn('joy', data['emotions'])

if __name__ == '__main__':
    unittest.main()
