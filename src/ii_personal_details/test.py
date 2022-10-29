import io
import unittest
from unittest.mock import patch

class TestClass(unittest.TestCase):
  @patch('sys.stdout', new_callable=io.StringIO)
  @patch('builtins.input', side_effect=['John', '27', '1.78'])
  def test_prints_user_details(self, mock_input, mock_out):
    from src.ii_personal_details import main
    self.assertEqual(mock_out.getvalue().strip(), 'Hola John\nUsted mide 1.78 y tiene 27 años')

if __name__ == '__main__':
  unittest.main()
