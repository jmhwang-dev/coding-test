def get_max_weight(N=2, ropes=[10, 15]):
    desc_sorted_ropes = sorted(ropes, reverse=True)
    max_weight = desc_sorted_ropes[0]
    if N == 1:
        return max_weight
    
    for i, weight in enumerate(desc_sorted_ropes[1:], 2):
        tmp_weight = weight * i
        if max_weight < tmp_weight:
            max_weight = tmp_weight

    return max_weight
        
            
N = int(input())
ropes = [int(input()) for _ in range(N)]
print(get_max_weight(N, ropes))

# print(get_max_weight())