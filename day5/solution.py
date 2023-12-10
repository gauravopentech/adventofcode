#!/usr/bin/python3
import unittest


filename = "input.txt"
# filename = "testinput.txt"


def extract_seeds(line):
    _, ids = line.split(":")
    id_list = ids.strip().split()
    # keeping both key values same because
    # it will help in handling one edge case
    # of converting src mapped values
    id_list = {int(x): int(x) for x in id_list}
    return id_list


def extract_seed_range(line):
    _, ids = line.split(":")
    id_list = ids.strip().split()
    # keeping both key values same because
    # it will help in handling one edge case
    # of converting src mapped values
    i = 0
    len_list = len(id_list)
    nlist = dict()
    while i < len_list:
        nlist[int(id_list[i])] = int(id_list[i + 1])
        i += 2

    return nlist


def find_and_udpate_mapped_value(src_ids, src, dest, inc):
    for sid in src_ids:
        if src_ids[sid] is None:
            if src <= sid < src + inc:
                src_ids[sid] = dest + (sid - src)


def get_new_src_ids(src_ids):
    new_src = dict()
    for sid in src_ids:
        if src_ids[sid] is not None:
            new_src[src_ids[sid]] = None
        else:
            new_src[sid] = None
    return new_src


def sol_one():
    min_loc = 0
    with open(filename) as infile:
        first_line = infile.readline()
        source_ids = extract_seeds(first_line)
        for line in infile:
            if len(line.strip()) == 0:
                source_ids = get_new_src_ids(source_ids)
            elif "map" in line:
                continue
            else:
                dest, src, inc = map(int, line.split())
                find_and_udpate_mapped_value(source_ids, src, dest, inc)
        source_ids = get_new_src_ids(source_ids)
        min_loc = min(source_ids.keys())
        print("Min source ids", min_loc)

    return min_loc


def find_and_udpate_mapped_range(src_ids, mapsrc_start, dest, inc):
    orig_dict = dict(src_ids)
    for sid in orig_dict:
        value = src_ids[sid]
        if isinstance(value, int):
            map_src_end = mapsrc_start + inc
            src_start = sid
            src_end = sid + value

            # case 1 where src start is between map src start and end
            if mapsrc_start <= src_start < map_src_end:
                src_start_diff = src_start - mapsrc_start
                src_end_diff = src_end - map_src_end
                if src_end_diff > 0:
                    src_ids[sid] = (dest + src_start_diff, map_src_end - src_start + 1)
                    src_ids[sid + map_src_end - src_start + 1] = src_end_diff
                else:
                    src_ids[sid] = (dest + src_start_diff, value)

            # case 2 where map src start is between src start and end
            elif src_start < mapsrc_start <= src_end:
                src_start_diff = mapsrc_start - src_start
                src_end_diff = map_src_end - src_end

                # start diff is always positive
                src_ids[sid] = src_start_diff
                if src_end_diff >= 0:
                    src_ids[sid + src_start_diff] = (dest, src_end - mapsrc_start + 1)
                else:
                    src_ids[sid + src_start_diff] = (dest, inc)
                    src_ids[sid + inc] = src_end - map_src_end + 1


def get_new_src_range(src_ids):
    new_src = dict()
    for sid in src_ids:
        value = src_ids[sid]
        if isinstance(value, tuple):
            dest, inc = value
            new_src[dest] = inc
        else:
            new_src[sid] = src_ids[sid]
    return new_src


def sol_two():
    min_loc = 0
    with open(filename) as infile:
        first_line = infile.readline()
        source_ids = extract_seed_range(first_line)
        for line in infile:
            if len(line.strip()) == 0:
                source_ids = get_new_src_range(source_ids)
            elif "map" in line:
                continue
            else:
                dest, src, inc = map(int, line.split())
                find_and_udpate_mapped_range(source_ids, src, dest, inc)
        source_ids = get_new_src_range(source_ids)
        min_loc = min(source_ids.keys())
        print("Min source ids", min_loc)

    return min_loc


class Test(unittest.TestCase):
    def test_extract_seeds(self):
        self.assertEqual(extract_seeds("Seeds: 3 4 1 5"), {3: 3, 4: 4, 1: 1, 5: 5})

    def test_find_and_udpate_mapped_value(self):
        source_ids = {3: None, 4: None, 1: None, 5: None}
        find_and_udpate_mapped_value(source_ids, 3, 9, 2)
        self.assertEqual(source_ids, {3: 9, 4: 10, 1: None, 5: None})

    def test_get_new_src_ids(self):
        source_ids = {3: 9, 4: 10, 1: None, 5: None}
        self.assertEqual(
            get_new_src_ids(source_ids), {9: None, 10: None, 1: None, 5: None}
        )

    def test_extract_seed_range(self):
        self.assertEqual(extract_seed_range("Seeds: 3 4 1 5"), {3: 4, 1: 5})


if __name__ == "__main__":
    # unittest.main()
    # sol_one()
    sol_two()
