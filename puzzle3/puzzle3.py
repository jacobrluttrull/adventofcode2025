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


def find_total_joltage_part_2():
    total = 0
    with open('input.txt') as file:
        for line in file:
            line = line.strip()
            stack = []
            digits_to_remove = len(line) - 12

            for digit in line:
                while stack and digit > stack[-1] and digits_to_remove > 0:
                    stack.pop()
                    digits_to_remove -= 1
                stack.append(digit)

            while digits_to_remove > 0:
                stack.pop()
                digits_to_remove -= 1

            result = ''.join(stack)
            total += int(result)

    return total


print(find_total_joltage_part_2())




print(find_highest_joltage())
print(find_total_joltage_part_2())