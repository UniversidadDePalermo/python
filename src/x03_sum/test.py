import io
import unittest
from unittest.mock import patch

class TestX03Sum(unittest.TestCase):
  @patch('sys.stdout', new_callable=io.StringIO)
  @patch('builtins.input', side_effect=['4', '2'])
  def test_adds_2_numbers(self, _, mock_out):
    from src.x03_sum import main
    self.assertEqual(mock_out.getvalue().strip(), 'El resultado es 6')

if __name__ == '__main__':
  unittest.main()
