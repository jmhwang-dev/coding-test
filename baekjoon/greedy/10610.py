def list2int(number_list):
    number_str = ''.join(map(str, number_list))
    return int(number_str)


def get_max_N(N="80875542"):
    numbers = list(map(lambda x: int(x), N))
    numbers = sorted(numbers, reverse=True)

    output = list2int(numbers)
    if output % 30 == 0:
        return output
    else:
        return -1

N = input()
print(get_max_N(N))