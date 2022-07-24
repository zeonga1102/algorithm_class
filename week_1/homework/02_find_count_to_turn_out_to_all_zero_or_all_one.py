input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    last_character = string[0]
    count = [0, 0]
    for i in string[1:]:
        if last_character != i:
            count[int(i)] += 1
        last_character = i
    return count[0] if count[0] < count[1] else count[1]


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)