def find_highest_joltage():
    total = 0
    with open('input.txt') as file:
        for line in file:
            line = line.strip()
            max_joltage = 0
            for ones_pos in range(1, len(line)):
                tens_digit = max(line[0:ones_pos])
                ones_digit = line[ones_pos]
                joltage = int(tens_digit + ones_digit)
                max_joltage = max(max_joltage, joltage)
            total += max_joltage
    return total

print(find_highest_joltage())