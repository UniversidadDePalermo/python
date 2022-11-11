import io
import unittest
from unittest.mock import patch

from src.x64_bubble_sort.main import swap, bubble_sort

class TestX64BubbleSort(unittest.TestCase):
  def test_swap_numbers_in_vector(self):
    vec = [1, 2, 3, 4, 5]
    swap(vec, 1, 2)
    self.assertEqual(vec, [1, 3, 2, 4, 5])

  def test_bubble_sort(self):
    vec = [5, 4, 3, 2, 1]
    sorted = bubble_sort(vec)
    self.assertEqual(sorted, [1, 2, 3, 4, 5])

if __name__ == '__main__':
  unittest.main()
