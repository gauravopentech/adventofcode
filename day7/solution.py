#!/usr/bin/python3

import unittest
import heapq


class Solution:
    FIVE_OF_KIND = set([(5,)])
    FOUR_OF_KIND = set([(4, 1), (1, 4)])
    FULL_HOUSE = set([(3, 2), (2, 3)])
    THREE_OF_KIND = set([(3, 1, 1), (1, 3, 1), (1, 1, 3)])
    TWO_PAIRS = set([(2, 2, 1), (2, 1, 2), (1, 2, 2)])
    ONE_PAIR = set([(2, 1, 1, 1), (1, 2, 1, 1), (1, 1, 2, 1), (1, 1, 1, 2)])
    HIGH_CARD = set([(1, 1, 1, 1, 1)])

    card_strength_map = {
        "2": "H",
        "3": "I",
        "4": "J",
        "5": "K",
        "6": "L",
        "7": "M",
        "8": "N",
        "9": "O",
        "T": "P",
        "J": "Q",
        "Q": "R",
        "K": "S",
        "A": "T",
    }

    def __init__(self, filename, part_to_run=1):
        """
        :param filename: The name of the file to read input from
        :param part_to_run: The part of the solution to run (1 or 2)
        """
        self.filename = filename
        self.part_to_run = part_to_run

    def extract_input(self):
        with open(self.filename) as infile:
            for line in infile:
                hand, points = line.strip().split()
                yield hand, points

    def run(self):
        if self.part_to_run == 1:
            return self.sol_one()
        elif self.part_to_run == 2:
            return self.sol_two()
        else:
            return "Invalid part to run"

    def sol_one(self):
        def normalize_hand(hand):
            newhand = ""
            card_counts = {}
            for card in hand:
                newhand += Solution.card_strength_map[card]
                card_counts[card] = card_counts.get(card, 0) + 1

            countset = tuple(card_counts.values())
            if countset in Solution.FIVE_OF_KIND:
                newhand = "G" + newhand
            elif countset in Solution.FOUR_OF_KIND:
                newhand = "F" + newhand
            elif countset in Solution.FULL_HOUSE:
                newhand = "E" + newhand
            elif countset in Solution.THREE_OF_KIND:
                newhand = "D" + newhand
            elif countset in Solution.TWO_PAIRS:
                newhand = "C" + newhand
            elif countset in Solution.ONE_PAIR:
                newhand = "B" + newhand
            else:
                newhand = "A" + newhand
            # print(f"{hand} -> {newhand}, {card_counts}")
            return newhand

        normalhands = []
        for hand, points in self.extract_input():
            normhand = normalize_hand(hand)
            normalhands.append((normhand, points, hand))

        normalhands.sort(key=lambda x: x[0])

        pointsum = 0
        for i in range(len(normalhands)):
            normh, point, hand = normalhands[i]
            currval = (i + 1) * int(point)
            pointsum += currval

        return pointsum

    def sol_two(self):
        def normalize_hand(hand):
            newhand = ""
            card_counts = {}
            for card in hand:
                newhand += Solution.card_strength_map[card]
                card_counts[card] = card_counts.get(card, 0) + 1
            found_j = False
            if "J" in card_counts:
                found_j = True

            countset = tuple(card_counts.values())
            if countset in Solution.FIVE_OF_KIND:
                rank = "G"
            elif countset in Solution.FOUR_OF_KIND:
                rank = "G" if found_j else "F"
            elif countset in Solution.FULL_HOUSE:
                rank = "G" if found_j else "E"
            elif countset in Solution.THREE_OF_KIND:
                rank = "F" if found_j else "D"
            elif countset in Solution.TWO_PAIRS:
                rank = "C"
                if card_counts.get("J") == 1:
                    rank = "E"
                elif card_counts.get("J") == 2:
                    rank = "F"
            elif countset in Solution.ONE_PAIR:
                rank = "D" if found_j else "B"
            else:
                rank = "B" if found_j else "A"
            newhand = rank + newhand
            return newhand

        normalhands = []
        Solution.card_strength_map["J"] = "F"
        for hand, points in self.extract_input():
            normhand = normalize_hand(hand)
            normalhands.append((normhand, points, hand))

        normalhands.sort(key=lambda x: x[0])

        pointsum = 0
        for i in range(len(normalhands)):
            normh, point, hand = normalhands[i]
            currval = (i + 1) * int(point)
            pointsum += currval

        return pointsum


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution("testinput.txt")

    def test_one(self):
        self.assertEqual(self.solution.sol_one(), 6440)

    def test_five_of_kind(self):
        hand = "AAAAA"
        self.assertEqual(Solution.normalize_hand(hand), "GTTTTT")

    def test_two(self):
        self.assertEqual(1, 1)


if __name__ == "__main__":
    solution = Solution("input.txt", 2)
    print(solution.run())
