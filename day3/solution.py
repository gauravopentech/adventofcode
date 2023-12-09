#!/usr/bin/python3

import unittest


def readFile():
    with open("input.txt") as infile:
        for line in infile:
            yield line.strip()


def is_part(coordinate, symbol):
    for i in range(coordinate[0] - 1, coordinate[1] + 1):
        if i in symbol:
            return i

    return None


def extract_part_symbol(line):
    parts = []
    symbols = set()
    i = 0
    len_line = len(line)
    while i < len_line:
        if line[i].isdigit():
            start = i
            while i < len_line and line[i].isdigit():
                i += 1
            end = i
            parts.append([int(line[start:end]), (start, end)])
        else:
            if line[i] != ".":
                symbols.add(i)

            i += 1

    return parts, symbols


def sol_one():
    prev_line = next(readFile())
    prev_parts, prev_symbols = extract_part_symbol(prev_line)
    total = 0
    for line in readFile():
        curr_parts, curr_symbols = extract_part_symbol(line)
        sym_list = curr_symbols.union(prev_symbols)
        for part, coord in prev_parts:
            if is_part(coord, sym_list) is not None:
                total += part
        temp_part = list(curr_parts)
        for idx, item in enumerate(temp_part):
            part, coord = item
            if is_part(coord, sym_list) is not None:
                total += part
                # Overwriting with invalid values to avoid double counting
                curr_parts[idx] = [0, (-1, -1)]
        prev_parts = curr_parts
        prev_symbols = curr_symbols

    return total


def extract_part_star(line):
    parts = []
    star = set()
    i = 0
    len_line = len(line)
    while i < len_line:
        if line[i].isdigit():
            start = i
            while i < len_line and line[i].isdigit():
                i += 1
            end = i
            parts.append([int(line[start:end]), (start, end)])
        else:
            if line[i] == "*":
                star.add(i)

            i += 1

    return parts, star


def update_potential_gears(prev_parts, sym_list, idx, potential_gears):
    for part, coord in prev_parts:
        nearest_star = is_part(coord, sym_list)
        if nearest_star is not None:
            star_idx = (idx, nearest_star)
            potential_gears[star_idx] = potential_gears.get(star_idx, []) + [part]
    return potential_gears


def sol_two():
    prev_line = next(readFile())
    prev_parts, prev_stars = extract_part_star(prev_line)
    total = 0
    potential_gears = dict()
    for idx, line in enumerate(readFile()):
        curr_parts, curr_stars = extract_part_star(line)
        update_potential_gears(curr_parts, prev_stars, idx - 1, potential_gears)

        update_potential_gears(prev_parts, curr_stars, idx, potential_gears)

        update_potential_gears(curr_parts, curr_stars, idx, potential_gears)

        prev_parts = curr_parts
        prev_stars = curr_stars

    print(potential_gears)
    for key, value in potential_gears.items():
        if len(value) == 2:
            total += value[0] * value[1]
    return total


class TestSolution(unittest.TestCase):
    def test_number_extract(self):
        parts, _ = extract_part_symbol("...123...456...")
        self.assertEqual(parts[0], [123, (3, 6)])
        self.assertEqual(parts[1], [456, (9, 12)])

    def test_symbol_extract(self):
        _, symbol = extract_part_symbol("...123.*.45#...")
        self.assertTrue(7 in symbol)
        self.assertTrue(11 in symbol)

    def test_is_part(self):
        coordinate = (3, 6)
        symbols = {2, 11}
        ispart = is_part(coordinate, symbols)
        self.assertEqual(ispart, 2)

        coordinate = (3, 6)
        symbols = {6, 11}
        ispart = is_part(coordinate, symbols)
        self.assertEqual(ispart, 6)

        coordinate = (3, 6)
        symbols = {3, 11}
        ispart = is_part(coordinate, symbols)
        self.assertEqual(ispart, 3)

    def test_is_not_part(self):
        coordinate = (3, 6)
        symbols = {1, 11}
        ispart = is_part(coordinate, symbols)
        self.assertIsNone(ispart)

        coordinate = (3, 6)
        symbols = {7, 11}
        ispart = is_part(coordinate, symbols)
        self.assertIsNone(ispart)

    def test_star_gear_extract(self):
        parts, stars = extract_part_star("...123.*.456..#..(..789..")
        _, symbol = extract_part_symbol("...123.*.456..#..(..789..")

        self.assertEqual(parts[0], [123, (3, 6)])
        self.assertEqual(parts[1], [456, (9, 12)])
        self.assertEqual(parts[2], [789, (20, 23)])

        self.assertTrue(7 in stars)
        self.assertFalse(14 in stars)
        self.assertFalse(17 in stars)

    def test_potential_gears(self):
        parts = [[123, (3, 6)], [456, (9, 12)], [789, (13, 16)]]
        sym_list = {1, 12}
        idx = 1
        potential_gears = dict(
            {
                (1, 12): [371],
            }
        )
        update_potential_gears(parts, sym_list, idx, potential_gears)
        self.assertFalse((1, 1) in potential_gears)
        self.assertTrue((1, 12) in potential_gears)
        self.assertEqual(potential_gears[(1, 12)], [371, 456, 789])


if __name__ == "__main__":
    # unittest.main()
    # print(sol_one())
    print(sol_two())
