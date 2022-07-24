input = 20


def find_prime_list_under_number(number):
    prime_numbers = []
    for i in range(number):
        if i == 2:
            prime_numbers.append(i)
            continue

        if i <= 1 or i % 2 == 0:
            continue

        for j in range(2, int(i/2)+1):
            if i % j == 0:
                break
        else:
            prime_numbers.append(i)

    return prime_numbers


result = find_prime_list_under_number(input)
print(result)