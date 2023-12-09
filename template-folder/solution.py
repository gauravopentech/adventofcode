#!/usr/bin/python3
import unittest


def readFile():
    with open("input.txt") as infile:
        for line in infile:
            yield line.strip()


def sol_one():
    for line in readFile():
        print(line)


def sol_two():
    for line in readFile():
        print(line)


class Test(unittest.TestCase):
    def test_one(self):
        self.assertEqual(1, 1)

    def test_two(self):
        self.assertEqual(1, 1)


if __name__ == "__main__":
    unittest.main()
    # sol_one()
    # sol_two()
