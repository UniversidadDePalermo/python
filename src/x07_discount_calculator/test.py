import io
import unittest
from unittest.mock import patch

from src.x07_discount_calculator.main import main

class TestX07DiscountCalculator(unittest.TestCase):
  @patch('sys.stdout', new_callable=io.StringIO)
  @patch('builtins.input', side_effect=['150'])
  def test_calculates_from_og_price(self, _, mock_out):
    main()
    self.assertEqual(mock_out.getvalue(), 'Precio original: 150 AR$\nPrecio a pagar abonando en efectivo: 135.0 AR$\n')

  @patch('sys.stdout', new_callable=io.StringIO)
  @patch('builtins.input', side_effect=['0'])
  def test_calculate_with_zero(self, _, mock_out):
    main()
    self.assertEqual(mock_out.getvalue(), 'Precio original: 0 AR$\nPrecio a pagar abonando en efectivo: 0.0 AR$\n')

if __name__ == '__main__':
  unittest.main()
