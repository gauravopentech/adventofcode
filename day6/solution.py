#!/usr/bin/python3
import unittest

filename = "input.txt"
# filename = "testinput.txt"


def extract(line):
    _, param_str = line.split(":")
    return param_str.split()


def readfile():
    with open(filename) as infile:
        race_times = extract(infile.readline())
        race_best_distance = extract(infile.readline())
    return race_times, race_best_distance


def is_winning_speed_fn(time, best_distance):
    def comparator(charge_time):
        distance_covered = charge_time * (time - charge_time)
        return distance_covered > best_distance

    return comparator


def binary_search(comparator, start, end):
    """
    Think about using Binary search to solve the problem
    """
    pass


def brute_search(comparator, duration):
    start = 0
    for i in range(duration):
        if comparator(i):
            start = i
            break

    return duration + 1 - (2 * start)


def sol_one():
    total = 1
    race_times, race_best_distance = readfile()
    for duration, best_distance in zip(race_times, race_best_distance):
        duration, best_distance = int(duration), int(best_distance)
        comparator = is_winning_speed_fn(duration, best_distance)
        ways_to_win = brute_search(comparator, duration)
        total *= ways_to_win

    return total


def sol_two():
    race_times, race_best_distance = readfile()
    duration = int("".join(race_times))
    best_distance = int("".join(race_best_distance))
    comparator = is_winning_speed_fn(duration, best_distance)
    ways_to_win = brute_search(comparator, duration)

    return ways_to_win


class Test(unittest.TestCase):
    def test_comparator(self):
        comparator = is_winning_speed_fn(7, 9)
        self.assertTrue(comparator(2))
        self.assertTrue(comparator(3))
        self.assertTrue(comparator(4))
        self.assertTrue(comparator(5))
        self.assertFalse(comparator(0))
        self.assertFalse(comparator(1))
        self.assertFalse(comparator(6))
        self.assertFalse(comparator(7))

    def test_brute_search(self):
        comparator = is_winning_speed_fn(7, 9)
        res = brute_search(comparator, 7)
        self.assertEqual(res, 4)

        comparator = is_winning_speed_fn(15, 40)
        res = brute_search(comparator, 15)
        self.assertEqual(res, 8)

        comparator = is_winning_speed_fn(30, 200)
        res = brute_search(comparator, 30)
        self.assertEqual(res, 9)

    def test_sol_one(self):
        res = sol_one()
        self.assertEqual(res, 2065338)

    def test_sol_two(self):
        res = sol_two()
        self.assertEqual(res, 34934171)


if __name__ == "__main__":
    # res = sol_one()
    res = sol_two()
    print(res)
