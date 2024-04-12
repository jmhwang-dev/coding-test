def get_min_flip(S="11001100110011000001"):
    flag = S[0]
    arr = [0, 0]
    for num in S[1:]:
        if flag == num:
            continue
        arr[int(flag)] += 1
        flag = num
    arr[int(flag)] += 1
    return min(arr)
    pass
S = input()
print(get_min_flip(S))