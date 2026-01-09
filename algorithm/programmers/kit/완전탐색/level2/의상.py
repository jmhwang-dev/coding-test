# hash
def solution(clothes):
    answer = 1
    
    clothes_dict = {}
    
    for cloth in clothes:
        name, category = cloth
        if category in clothes_dict:
            clothes_dict[category].append(name)
        else:
            clothes_dict[category] = [name]
            
    for names in clothes_dict.values():
        answer *= (len(names) + 1)
    
    return answer - 1

# Counter
from collections import Counter

def solution(clothes):
    counter = Counter([kind for name, kind in clothes])
    
    answer = 1
    for count in counter.values():
        answer *= (count + 1)
    
    return answer - 1