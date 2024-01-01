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
            directions = lines[0].strip()
            network = {}
            for line in lines[2:]:
                loc, options = line.split("=")
                loc = loc.strip()
                options = options.strip()
                network[loc] = {"L": options[1:4], "R": options[6:9]}

        return directions, network

    def run(self):
        if self.part_to_run == 1:
            return self.sol_one()
        elif self.part_to_run == 2:
            return self.sol_two()
        else:
            return "Invalid part to run"

    def get_next_direction(self, direction):
        len_dir = len(direction)
        i = 0
        while True:
            yield direction[i % len_dir]
            i += 1

    def sol_one(self):
        directions, network = self.extract_input()
        curr_loc = "AAA"
        end = "ZZZ"
        turn_count = 0
        for direction in self.get_next_direction(directions):
            curr_loc = network[curr_loc][direction]
            turn_count += 1
            if curr_loc == end:
                break

        return turn_count

    def sol_two(self):
        import math

        directions, network = self.extract_input()
        curr_locs = filter(lambda x: x[-1] == "A", network.keys())

        def find_turn_count(curr_loc):
            turn_count = 0
            for direction in self.get_next_direction(directions):
                curr_loc = network[curr_loc][direction]
                turn_count += 1
                if curr_loc[-1] == "Z":
                    break

            return turn_count

        loc_turn_counts = list(map(find_turn_count, curr_locs))
        return math.lcm(*loc_turn_counts)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution("testinput.txt")

    def test_one(self):
        self.assertEqual(1, 1)

    def test_two(self):
        self.assertEqual(1, 1)


if __name__ == "__main__":
    solution = Solution("input.txt", 2)
    print(solution.run())
