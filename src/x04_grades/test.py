import io
import unittest
from unittest.mock import patch

from src.x04_grades.main import main

class TestX04Grades(unittest.TestCase):
  @patch('sys.stdout', new_callable=io.StringIO)
  @patch('builtins.input', side_effect=['10', '10', '10'])
  def test_is_abanderado(self, _, mock_out):
    main()
    self.assertEqual(mock_out.getvalue().strip(), 'Abanderado')

  @patch('sys.stdout', new_callable=io.StringIO)
  @patch('builtins.input', side_effect=['7', '7', '7'])
  def test_is_aprobado(self, _, mock_out):
    main()
    self.assertEqual(mock_out.getvalue().strip(), 'Aprobado')

  @patch('sys.stdout', new_callable=io.StringIO)
  @patch('builtins.input', side_effect=['7', '6', '3'])
  def test_is_diciembre(self, _, mock_out):
    main()
    self.assertEqual(mock_out.getvalue().strip(), 'Diciembre')

  @patch('sys.stdout', new_callable=io.StringIO)
  @patch('builtins.input', side_effect=['2', '2', '3'])
  def test_is_marzo(self, _, mock_out):
    main()
    self.assertEqual(mock_out.getvalue().strip(), 'Marzo')

if __name__ == '__main__':
  unittest.main()
