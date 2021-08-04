from app import app, get_currency,cc, cr
from unittest import TestCase


class AdditionTestCase(TestCase):

    def test_get_currency(self):
        # with app.test_client() as client:
        self.assertEqual(cc.get_symbol('GBP'),'£')
        self.assertEqual(cr.convert("USD", "USD", 1), 1)
        self.assertEqual(cr.convert("GBP", "GBP", 1), 1)


        
    