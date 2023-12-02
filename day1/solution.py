#!/usr/bin/python3


def readFile():
    with open("input.txt") as infile:
        for line in infile:
            yield line.strip()


def get_first_digit(string):
    for char in string:
        if char.isdigit():
            return char


def parsed_str(string):
    digits_str = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    digit_initials = {
        "o": ["one"],
        "t": ["two", "three"],
        "f": ["four", "five"],
        "s": ["six", "seven"],
        "e": ["eight"],
        "n": ["nine"],
    }
    calib = ""
    found = False
    for idx, char in enumerate(string):
        if char.isdigit():
            calib = char
            found = True
        if char in digit_initials:
            for digit in digit_initials[char]:
                if string[idx : idx + len(digit)] == digit:
                    calib = str(digits_str[digit])
                    found = True
        if found:
            break
    len_str = len(string)
    found = False
    for idx, char in enumerate(reversed(string)):
        if char.isdigit():
            calib += char
            found = True
        if char in digit_initials:
            for digit in digit_initials[char]:
                norm_idx = len_str - idx - 1
                if string[norm_idx : norm_idx + len(digit)] == digit:
                    calib += str(digits_str[digit])
                    found = True
        if found:
            break

    return calib


def sol_one():
    total = 0
    for line in readFile():
        fist_digit = get_first_digit(line)
        last_digit = get_first_digit(reversed(line))
        total += int(f"{fist_digit}{last_digit}")
    print(total)


def sol_two():
    total = 0
    for line in readFile():
        total += int(parsed_str(line))
    print(total)


# sol_one()
sol_two()
