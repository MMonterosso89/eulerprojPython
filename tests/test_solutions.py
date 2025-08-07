import unittest
from solutions.ID_1 import three_five_divis_total, sum_of_multiples
from solutions.ID_2 import fib_sum, even_fibonacci_sum

class TestSolutions(unittest.TestCase):
    def test_id_1(self):
        # The user's solution has been refactored to be more idiomatic.
        self.assertEqual(three_five_divis_total(1000), 233168)
        self.assertEqual(sum_of_multiples(1000), 233168)

    def test_id_2(self):
        self.assertEqual(fib_sum(4_000_000), 4613732)
        self.assertEqual(even_fibonacci_sum(4_000_000), 4613732)

if __name__ == '__main__':
    unittest.main()
