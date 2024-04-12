def get_min_pocket(kilogram=11):
    count = 0
    total = kilogram
    while True:
        remainder = total - 3
        count += 1
        if total % 5 == 0:
            return total // 5
        elif remainder % 5 == 0:
            return remainder // 5 + count
        elif remainder < 0:
            return -1
        total = remainder

N = int(input())
print(get_min_pocket(N))