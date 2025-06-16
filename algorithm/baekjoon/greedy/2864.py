def get_min(number="16796"):
    return int(number.replace('6', '5'))

def get_max(number="58786"):
    return int(number.replace('5', '6'))

A, B = input().split()
min_A = get_min(A)
max_A = get_max(A)

min_B = get_min(B)
max_B = get_max(B)
print(min_A + min_B, max_A + max_B)