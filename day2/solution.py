#!/usr/bin/python3


def readFile():
    with open("input.txt") as infile:
        for line in infile:
            yield line.strip()


def parseLine(line):
    gameidx, ball_sets = line.split(":")
    _, game_id = gameidx.split()
    game_id = int(game_id)
    ball_sets = ball_sets.split(";")
    return game_id, ball_sets


def valid_game(game_id, ball_sets):
    available_ball_count = {"red": 12, "green": 13, "blue": 14}
    for ball_set in ball_sets:
        for ball in ball_set.split(","):
            ball_count, color = ball.split()
            balls = int(ball_count)
            if balls > available_ball_count[color]:
                game_id = 0
    return game_id


def sol_one():
    game_sum = 0
    for line in readFile():
        game_id, ball_sets = parseLine(line)
        game_id = valid_game(game_id, ball_sets)
        game_sum += game_id
    print(game_sum)


def power_cube(ball_sets):
    min_required = {"red": 0, "green": 0, "blue": 0}
    for ball_set in ball_sets:
        for ball in ball_set.split(","):
            ball_count, color = ball.split()
            balls = int(ball_count)
            min_required[color] = max(min_required[color], balls)
    power_cube_val = 1
    for val in min_required.values():
        power_cube_val *= val
    return power_cube_val


def sol_two():
    cube_power_sum = 0
    for line in readFile():
        _, ball_sets = parseLine(line)
        cube_power = power_cube(ball_sets)
        cube_power_sum += cube_power
    print(cube_power_sum)


sol_one()
sol_two()
