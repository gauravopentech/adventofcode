#!/usr/bin/python3
import unittest


def get_level_0_nth(n, start):
    # Level 0 is where the differences are all 0
    return 0


def get_level_1_nth(n, start):
    # Level 1 is where the differences are all constant
    return start


def get_level_2_nth(n, start, diff):
    # Level 2 is where the differences are all in arithmatic progression
    # with a constant difference
    if n < 0:
        return 0
    level_1_first = get_level_1_nth(0, diff)
    return start + n * level_1_first


def get_level_3_nth(n, start, diff, diff_of_2):
    # Level 3 is where the differenc of differences are all in
    # arithmatic progression with a constant difference
    if n < 0:
        return 0

    level_2_first = get_level_2_nth(0, diff, diff_of_2)
    level_2_n_minus_1 = get_level_2_nth(n - 1, diff, diff_of_2)
    return start + (n / 2) * (level_2_first + level_2_n_minus_1)


def get_level_4_nth(n, start, diff, diff_of_2, diff_of_3):
    # Level 3 is where the differenc of differences are all in
    # arithmatic progression with a constant difference
    level_3_first = get_level_3_nth(0, diff, diff_of_2, diff_of_3)
    level_2_first = get_level_2_nth(0, diff_of_2, diff_of_3)
    level_2_n_minus_2 = get_level_2_nth(n - 2, diff_of_2, diff_of_3)

    if n < 1:
        level_2_first = 0

    nth_value = (
        start
        + (n) * level_3_first
        + (n * (n - 1)) / 2 * level_2_first
        + (n - 2) / 2 * (level_2_first + level_2_n_minus_2)
    )

    return nth_value


class TestSolution(unittest.TestCase):
    def test_one(self):
        # Testing series 3, 9, 15, 21, 27, 33, 39, 45, 51, 57
        self.assertEqual(get_level_2_nth(0, 3, 6), 3)
        self.assertEqual(get_level_2_nth(1, 3, 6), 10)

    def test_two(self):
        # testing series 1 3 6 10 15 21
        self.assertEqual(get_level_3_nth(0, 1, 2, 1), 1)
        self.assertEqual(get_level_3_nth(1, 1, 2, 1), 3)
        self.assertEqual(get_level_3_nth(2, 1, 2, 1), 6)
        self.assertEqual(get_level_3_nth(3, 1, 2, 1), 10)


if __name__ == "__main__":
    for i in range(10):
        print(get_level_4_nth(i, 10, 3, 0, 2))
