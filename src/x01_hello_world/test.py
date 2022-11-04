import io
import unittest
from unittest.mock import patch

class TestX01HelloWorld(unittest.TestCase):
  @patch('sys.stderr', new_callable=io.StringIO)
  @patch('sys.stdout', new_callable=io.StringIO)
  def test_prints_hello_world(self, mock_out, mock_err):
    from src.x01_hello_world import main
    self.assertEqual(mock_out.getvalue().strip(), 'Hello World')

if __name__ == '__main__':
  unittest.main()
