from app import app
from unittest import TestCase


class AdditionTestCase(TestCase):

    def test_get_currency(self):
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code,200)
            self.assertIn(' <title>home</title>', html)
       
    