import io
import unittest
from unittest.mock import patch

from src.x06_salary_calculator.main import main

class TestX06SalaryCalculator(unittest.TestCase):
  @patch('sys.stdout', new_callable=io.StringIO)
  @patch('builtins.input', side_effect=['150.00', '120'])
  def test_calculates_as_example(self, _, mock_out):
    main()
    self.assertEqual(mock_out.getvalue().strip(), 'El sueldo por 120 al mes es de 18000.0 AR$')

  @patch('sys.stdout', new_callable=io.StringIO)
  @patch('builtins.input', side_effect=['0', '120'])
  def test_supports_zero(self, _, mock_out):
    main()
    self.assertEqual(mock_out.getvalue().strip(), 'El sueldo por 120 al mes es de 0.0 AR$')

if __name__ == '__main__':
  unittest.main()
