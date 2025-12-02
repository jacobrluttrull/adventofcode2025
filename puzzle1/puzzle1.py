import math


def calc_password_part1(dial_pos, amount_hits_0):
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            direction = line[0]
            distance = int(line[1:])

            if direction == "R":
                dial_pos = (dial_pos + distance) % 100
            else:
                dial_pos = (dial_pos - distance) % 100

            if dial_pos == 0:
                amount_hits_0 += 1

    return amount_hits_0
def calc_password_part2(amount_hits_0):
    abs_pos = 50

    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            direction = line[0]
            distance = int(line[1:])

            prev = abs_pos

            if direction == "R":
                abs_pos = prev + distance
                # positions visited: prev+1 .. abs_pos
                start_block = prev // 100
                end_block = abs_pos // 100
                hits_this_move = end_block - start_block

            else:  # "L"
                abs_pos = prev - distance
                # positions visited: prev-1 .. abs_pos
                start_block = (prev - 1) // 100
                end_block = (abs_pos - 1) // 100
                hits_this_move = start_block - end_block

            amount_hits_0 += hits_this_move

    return amount_hits_0



dial_pos = 50
amount_hits_0 = 0

result = calc_password_part1(dial_pos, amount_hits_0)
password = calc_password_part2(amount_hits_0)
print(result)
print(password)
