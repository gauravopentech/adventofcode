#!/usr/bin/python3
import unittest


class Solution:
    def __init__(self, filename, part_to_run=1):
        """
        :param filename: The name of the file to read input from
        :param part_to_run: The part of the solution to run (1 or 2)
        """
        self.filename = filename
        self.part_to_run = part_to_run

    def extract_input(self):
        with open(self.filename) as infile:
            lines = infile.readlines()
        return lines

    def run(self):
        if self.part_to_run == 1:
            return self.sol_one()
        elif self.part_to_run == 2:
            return self.sol_two()
        else:
            return "Invalid part to run"

    def sol_one(self):
        input = self.extract_input()
        return input

    def sol_two(self):
        input = self.extract_input()
        return input


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution("testinput.txt")

    def test_one(self):
        self.assertEqual(1, 1)

    def test_two(self):
        self.assertEqual(1, 1)


if __name__ == "__main__":
    solution = Solution("input.txt", 1)
    print(solution.run())
