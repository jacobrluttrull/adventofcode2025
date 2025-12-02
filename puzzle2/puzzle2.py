def is_invalid(id_str):
    for pattern_length in range(1, len(id_str) // 2 + 1):
        pattern = id_str[:pattern_length]
        repetitions = len(id_str) // pattern_length
        if repetitions >= 2 and pattern * repetitions == id_str:
            return True
    return False


list_of_invalid_ids = []
list_of_invalid_ids2 = []

with open("input.txt") as file:
    content = file.read()

ranges = content.split(",")

# Part 1
for range_str in ranges:
    range_str = range_str.strip()
    start_range, end_range = map(int, range_str.split("-"))

    start_length = len(str(start_range))
    end_length = len(str(end_range))

    for length in range(start_length, end_length + 1):
        if length % 2 == 0:
            pattern_length = length // 2
            for pattern_num in range(0, 10 ** pattern_length):
                pattern_str = str(pattern_num).zfill(pattern_length)
                if pattern_str[0] == '0':
                    continue

                full_id_str = pattern_str + pattern_str
                full_id = int(full_id_str)

                if start_range <= full_id <= end_range:
                    list_of_invalid_ids.append(full_id)

# Part 2
for range_str in ranges:
    range_str = range_str.strip()
    start_range, end_range = map(int, range_str.split("-"))

    for id_num in range(start_range, end_range + 1):
        if is_invalid(str(id_num)):
            list_of_invalid_ids2.append(id_num)

total = sum(list_of_invalid_ids)
total2 = sum(list_of_invalid_ids2)
print(f"Part 1: {total}")
print(f"Part 2: {total2}")