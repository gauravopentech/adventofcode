#!/usr/bin/python3
import unittest

filename = "input.txt"
# filename = "testinputs.txt"


def readFile():
    with open(filename) as infile:
        for line in infile:
            yield line.strip()


def extract_numbers(line):
    _, numbers = line.split(":")
    left, right = numbers.split("|")
    left, right = left.split(), right.split()
    return set(left), set(right)


def sol_one():
    total = 0
    for line in readFile():
        left, right = extract_numbers(line)
        matched = len(left.intersection(right))
        total += matched and 2 ** (matched - 1)
    return total


def sol_two():
    total = 0
    copies = dict()
    for idx, line in enumerate(readFile()):
        left, right = extract_numbers(line)
        matched = len(left.intersection(right))
        orig_and_copies = copies.get(idx, 0) + 1  # adding 1 for the original
        for i in range(matched):
            norm_idx = idx + i + 1
            copies[norm_idx] = (copies.get(norm_idx, 0)) + orig_and_copies
        total += orig_and_copies
    return total


class Test(unittest.TestCase):
    def test_extraction(self):
        line = "Card 1: 42 8 15 16 23 42 | 21 25 31 44 76 91 15 42"
        left, right = extract_numbers(line)
        self.assertEqual(left, {"42", "8", "15", "16", "23", "42"})

        self.assertEqual(right, {"21", "25", "31", "44", "76", "91", "15", "42"})

    def test_two(self):
        self.assertEqual(1, 1)


if __name__ == "__main__":
    torun = [
        # unittest.main,
        # sol_one,
        sol_two,
    ]
    for func in torun:
        res = func()
        print(func.__name__, res)
