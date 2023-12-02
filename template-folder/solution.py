#!/usr/bin/python3


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


sol_one()
# sol_two()
