def get_max_N(S=200):
    count = 0
    total = 0
    for i in range(1, 4294967295):
        total += i
        count += 1
        stop_number = i
        if total == S:
            return count
        elif total > S:
            break
    
    remainder = total - S
    if remainder < stop_number:
        return count - 1
    else: 
        return count

S = int(input())
print(get_max_N(S))