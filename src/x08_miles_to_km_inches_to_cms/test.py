import io
import unittest
from unittest.mock import patch

from src.x08_miles_to_km_inches_to_cms.main import main

class TestX08MilesToKmInchesToCms(unittest.TestCase):
  @patch('sys.stdout', new_callable=io.StringIO)
  @patch('builtins.input', side_effect=['x', '5'])
  def test_validates_op_type(self, _, mock_out):
    main()
    self.assertEqual(mock_out.getvalue(), 'La opción "x" no es valida. Debes ingresar "m" o "p"\n')

  @patch('sys.stdout', new_callable=io.StringIO)
  @patch('builtins.input', side_effect=['m', '5'])
  def test_convers_miles_to_km(self, _, mock_out):
    main()
    self.assertEqual(mock_out.getvalue(), '5.0 mi = 8.04675 km\n')

  @patch('sys.stdout', new_callable=io.StringIO)
  @patch('builtins.input', side_effect=['p', '5'])
  def test_inches_to_cms(self, _, mock_out):
    main()
    self.assertEqual(mock_out.getvalue(), '5.0″ = 12.669999999999998 cm\n')

if __name__ == '__main__':
  unittest.main()
