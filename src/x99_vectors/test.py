import io
import unittest
from unittest.mock import patch

from src.x99_vectors.main import make_vector_a, make_vector_b, promedio, add_nine_hundred_ninety_nine, get_max_value_pos, make_vector_c, add_two_hundred_twenty_two, remove_not_two_hundred_twenty_two

class TestX99Vectors(unittest.TestCase):
  @patch('builtins.input', side_effect=[12, 40, 14, 28, 50, 56, 58, 16, 20, 36])
  def test_make_vector_a_fills_10_elements(self, _):
    vector_a = make_vector_a()
    self.assertEqual(vector_a, [12, 40, 14, 28, 50, 56, 58, 16, 20, 36])
    self.assertEqual(len(vector_a), 10)

  @patch('sys.stdout', new_callable=io.StringIO)
  @patch('builtins.input', side_effect=[17, 12, 22, 1, 55, 55, 23, 14, 18 , 24, 15])
  def test_make_vector_a_disallow_out_of_range(self, _, mock_out):
    vector_a = make_vector_a()
    self.assertEqual(vector_a, [17, 12, 22, 55, 55, 23, 14, 18 , 24, 15])
    self.assertEqual(len(vector_a), 10)
    self.assertEqual(mock_out.getvalue(), 'El valor "1", no es válido. Debes ingresar un valor mayor o igual a 12 y menor a 60.\n')

  def test_promedio(self):
    vector_a = [12, 40, 14, 28, 50, 56, 58, 16, 20, 36]
    prom = promedio(vector_a)

    self.assertEqual(prom, 33)

  @patch('builtins.input', side_effect=[12, 40, 14, 28, 50, 56, 58, 16, 20, 36])
  def test_make_vector_with_values_gt_avg(self, _):
    vector_a = make_vector_a()
    vector_b = make_vector_b(vector_a)
    self.assertEqual(vector_b, [40, 50, 56, 58, 36])

  @patch('builtins.input', side_effect=[12, 40, 14, 28, 50, 56, 58, 16, 20, 36])
  def test_make_vector_with_nine_hundred_ninety_nine(self, _):
    vector_a = make_vector_a()
    vector_b = make_vector_b(vector_a)
    nine_hundred_ninety_nine = add_nine_hundred_ninety_nine(vector_b)
    self.assertEqual(vector_a, [12, 40, 14, 28, 50, 56, 58, 16, 20, 36])
    self.assertEqual(vector_b, [40, 50, 56, 58, 36])
    self.assertEqual(nine_hundred_ninety_nine, [40, 999, 50, 999, 56, 999, 58, 999, 36, 999])

  @patch('builtins.input', side_effect=[12, 40, 14, 28, 50, 56, 58, 16, 20, 36])
  def test_get_max_value_pos(self, _):
    vector_a = make_vector_a()
    max_value_pos = get_max_value_pos(vector_a)
    self.assertEqual(vector_a, [12, 40, 14, 28, 50, 56, 58, 16, 20, 36])
    self.assertEqual(max_value_pos, 6)

  @patch('builtins.input', side_effect=[12, 40, 14, 28, 50, 56, 58, 16, 20, 36])
  def test_make_vector_c(self, _):
    vector_a = make_vector_a()
    max_value_pos = get_max_value_pos(vector_a)
    vector_c = make_vector_c(vector_a)
    self.assertEqual(vector_a, [12, 40, 14, 28, 50, 56, 58, 16, 20, 36])
    self.assertEqual(max_value_pos, 6)
    self.assertEqual(vector_c, [12, 40, 14, 28, 50, 56])

  @patch('builtins.input', side_effect=[12, 40, 14, 28, 50, 56, 58, 16, 20, 36])
  def test_make_vector_with_two_hundred_twenty_two(self, _):
    vector_a = make_vector_a()
    max_value_pos = get_max_value_pos(vector_a)
    vector_c = make_vector_c(vector_a)
    two_hundred_twenty_two = add_two_hundred_twenty_two(vector_c)
    self.assertEqual(vector_a, [12, 40, 14, 28, 50, 56, 58, 16, 20, 36])
    self.assertEqual(max_value_pos, 6)
    self.assertEqual(vector_c, [12, 40, 14, 28, 50, 56])
    self.assertEqual(two_hundred_twenty_two, [12, 40, 14, 222, 28, 50, 222, 56])

  @patch('builtins.input', side_effect=[12, 40, 14, 28, 50, 56, 58, 16, 20, 36])
  def test_make_vector_with_two_hundred_twenty_two(self, _):
    vector_a = make_vector_a()
    max_value_pos = get_max_value_pos(vector_a)
    vector_c = make_vector_c(vector_a)
    two_hundred_twenty_two = add_two_hundred_twenty_two(vector_c)
    only_two_hundred_twenty_two = remove_not_two_hundred_twenty_two(two_hundred_twenty_two)
    self.assertEqual(vector_a, [12, 40, 14, 28, 50, 56, 58, 16, 20, 36])
    self.assertEqual(max_value_pos, 6)
    self.assertEqual(vector_c, [12, 40, 14, 28, 50, 56])
    self.assertEqual(two_hundred_twenty_two, [12, 40, 14, 222, 28, 50, 222, 56])
    self.assertEqual(only_two_hundred_twenty_two, [222, 222])

if __name__ == '__main__':
  unittest.main()
