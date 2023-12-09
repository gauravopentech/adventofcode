#!/usr/bin/python3
import unittest


def readFile():
    with open("input.txt") as infile:
        for line in infile:
            yield line.strip()


def sol_one():
    total = 0
    for line in readFile():
        print(line)
    return total


def sol_two():
    total = 0
    for line in readFile():
        print(line)
    return total


class Test(unittest.TestCase):
    def test_one(self):
        self.assertEqual(1, 1)

    def test_two(self):
        self.assertEqual(1, 1)


if __name__ == "__main__":
    unittest.main()
    # sol_one()
    # sol_two()
