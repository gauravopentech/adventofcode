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
        def get_diffs(input):
            diffs = []
            for i in range(1, len(input)):
                diffs.append(input[i] - input[i - 1])
            return diffs

        def is_predictable(diffs):
            return all(x == diffs[0] for x in diffs)

        input = self.extract_input()

        history_sum = 0
        for history in input:
            hist_list = list(map(int, history.split()))

            if self.part_to_run == 2:
                hist_list = list(reversed(hist_list))
            difflist = [hist_list]
            while not is_predictable(difflist[-1]):
                difflist.append(get_diffs(difflist[-1]))

            nextitem = 0
            while len(difflist) > 1:
                currdiff = difflist.pop()
                nextitem = difflist[-1][-1] + currdiff[-1]
                difflist[-1].append(nextitem)
            history_sum += nextitem

        return history_sum


if __name__ == "__main__":
    solution = Solution("input.txt", 2)
    print(solution.run())
