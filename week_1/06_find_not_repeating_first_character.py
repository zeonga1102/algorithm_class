input = "abadabac"

def find_not_repeating_character(string):
    for i in string:
        if string.count(i) == 1:
            return i
    return "_"


result = find_not_repeating_character(input)
print(result)