import unittest
from solutions.ID_1 import three_five_divis_total, sum_of_multiples
from solutions.ID_2 import fib_sum, even_fibonacci_sum
from solutions.ID_15 import lattice_paths
from solutions.ID_16 import power_digit_sum
from solutions.ID_17 import count_letters, number_to_words, total_letter_count
from solutions.ID_18 import parse_triangle, maximum_path_sum

class TestSolutions(unittest.TestCase):
    def test_id_1(self):
        # The user's solution has been refactored to be more idiomatic.
        self.assertEqual(three_five_divis_total(1000), 233168)
        self.assertEqual(sum_of_multiples(1000), 233168)

    def test_id_2(self):
        self.assertEqual(fib_sum(4_000_000), 4613732)
        self.assertEqual(even_fibonacci_sum(4_000_000), 4613732)

    def test_id_15(self):
        self.assertEqual(lattice_paths(2), 6)
        self.assertEqual(lattice_paths(20), 137846528820)

    def test_id_16(self):
        self.assertEqual(power_digit_sum(2, 15), 26)
        self.assertEqual(power_digit_sum(2, 1000), 1366)

    def test_id_17(self):
        self.assertEqual(total_letter_count(5), 19)
        self.assertEqual(count_letters(number_to_words(342)), 23)
        self.assertEqual(count_letters(number_to_words(115)), 20)
        self.assertEqual(total_letter_count(1000), 21124)

    def test_id_18(self):
        small_triangle_str = """
        3
        7 4
        2 4 6
        8 5 9 3
        """
        small_triangle = parse_triangle(small_triangle_str)
        self.assertEqual(maximum_path_sum(small_triangle), 23)

        large_triangle_str = """
        75
        95 64
        17 47 82
        18 35 87 10
        20 04 82 47 65
        19 01 23 75 03 34
        88 02 77 73 07 63 67
        99 65 04 28 06 16 70 92
        41 41 26 56 83 40 80 70 33
        41 48 72 33 47 32 37 16 94 29
        53 71 44 65 25 43 91 52 97 51 14
        70 11 33 28 77 73 17 78 39 68 17 57
        91 71 52 38 17 14 91 43 58 50 27 29 48
        63 66 04 68 89 53 67 30 73 16 69 87 40 31
        04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
        """
        large_triangle = parse_triangle(large_triangle_str)
        self.assertEqual(maximum_path_sum(large_triangle), 1074)

if __name__ == '__main__':
    unittest.main()
