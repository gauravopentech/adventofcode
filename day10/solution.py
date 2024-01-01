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
            lines = [list(line) for line in lines]
        return lines

    def run(self):
        if self.part_to_run == 1:
            return self.sol_one()
        elif self.part_to_run == 2:
            return self.sol_two()
        else:
            return "Invalid part to run"

    DIRECTIONS = {
        "-": [(0, 1), (0, -1) ],
        "|": [(1, 0), (-1, 0)],
        "J": [(0, -1), (-1, 0) ],
        "L": [(-1, 0), (0, 1) ],
        "F": [(1, 0), (0, 1) ],
        "7": [(1, 0), (0, -1) ],
    }

    def get_next_coords(self, grid, coords, prev_coord):
        x, y = coords
        currSym = grid[coords[0]][coords[1]]
        nextcor_f, nextcor_b = self.__class__.DIRECTIONS[currSym]
        coord_f = (x + nextcor_f[0], y + nextcor_f[1]) 
        coord_b = (x + nextcor_b[0], y + nextcor_b[1])
        return coord_f if coord_f != prev_coord else coord_b

    def sol_one(self):
        input = self.extract_input()
        start = (76, 109)  # location of S
        forward_coord= (76, 108)
        backward_coord = (75, 109)
        i = 1

        prev_f, prev_b = start, start
        while forward_coord != backward_coord:
            new_forward_coord = self.get_next_coords(input, forward_coord, prev_f)
            new_backward_coord = self.get_next_coords(input, backward_coord, prev_b)
            prev_f, prev_b = forward_coord, backward_coord
            forward_coord, backward_coord = new_forward_coord, new_backward_coord
            i += 1
        

        return i

    def sol_two(self):
        input = self.extract_input()
        start = (76, 109)  # location of S
        forward_coord= (76, 108)
        backward_coord = (75, 109)
        prev_f, prev_b = start, start
        while forward_coord != backward_coord:
            input[prev_f[0]][prev_f[1]] = 'X'
            input[prev_b[0]][prev_b[1]] = 'X'
            new_forward_coord = self.get_next_coords(input, forward_coord, prev_f)
            new_backward_coord = self.get_next_coords(input, backward_coord, prev_b)
            prev_f, prev_b = forward_coord, backward_coord
            forward_coord, backward_coord = new_forward_coord, new_backward_coord

        # with open('output.txt', 'w') as f:
        #     for line in input:
        #         f.write(''.join(line))
        rows = len(input)
        cols = len(input[0])
        for i in range(rows):
            is_in_loop = False
            curr_row = input[i]
            for j in range(cols):
                try:
                    if input[i][j] == 'X':
                        is_in_loop = not is_in_loop
                except IndexError:
                    pass
        i = 0
        return i


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution("testinput.txt")

    def test_directions(self):
        startx, starty = 76, 109

        # Horizontal
        # 76 + 0, 109 + 1
        # 76 + 0, 109 - 1
        dx, dy = self.solution.DIRECTIONS['-'][0]
        self.assertEqual((startx + dx, starty + dy), (76, 110))
        dx, dy = self.solution.DIRECTIONS['-'][1]
        self.assertEqual((startx + dx, starty + dy), (76, 108))

        # Vertical
        # 76 + 1, 109 + 0
        # 76 - 1, 109 + 0
        dx, dy = self.solution.DIRECTIONS['|'][0]
        self.assertEqual((startx + dx, starty + dy), (77, 109))
        dx, dy = self.solution.DIRECTIONS['|'][1]
        self.assertEqual((startx + dx, starty + dy), (75, 109))

        # left and up
        # 76 + 0, 109 - 1
        # 76 - 1, 109 + 0
        dx, dy = self.solution.DIRECTIONS['J'][0]
        self.assertEqual((startx + dx, starty + dy), (76, 108))
        dx, dy = self.solution.DIRECTIONS['J'][1]
        self.assertEqual((startx + dx, starty + dy), (75, 109))

        # left and down
        # 76 + 0, 109 - 1
        # 76 + 1, 109 + 0
        dx, dy = self.solution.DIRECTIONS['7'][0]
        self.assertEqual((startx + dx, starty + dy), (77, 109))
        dx, dy = self.solution.DIRECTIONS['7'][1]
        self.assertEqual((startx + dx, starty + dy), (76, 108))

        # right and up
        # 76 + 0, 109 + 1
        # 76 - 1, 109 + 0
        dx, dy = self.solution.DIRECTIONS['L'][0]
        self.assertEqual((startx + dx, starty + dy), (75, 109))
        dx, dy = self.solution.DIRECTIONS['L'][1]
        self.assertEqual((startx + dx, starty + dy), (76, 110))

        # right and down
        # 76 + 1, 109 + 0
        # 76 + 0, 109 + 1
        dx, dy = self.solution.DIRECTIONS['F'][0]
        self.assertEqual((startx + dx, starty + dy), (77, 109))
        dx, dy = self.solution.DIRECTIONS['F'][1]
        self.assertEqual((startx + dx, starty + dy), (76, 110))


    def test_one(self):
        self.assertEqual(1, 1)

    def test_two(self):
        self.assertEqual(1, 1)


if __name__ == "__main__":
    # unittest.main()
    solution = Solution("input.txt", 2)
    print(solution.run())
