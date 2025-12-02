def calc_amount(dial_pos, amount_hits_0):
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


dial_pos = 50
amount_hits_0 = 0

result = calc_amount(dial_pos, amount_hits_0)
print(result)
