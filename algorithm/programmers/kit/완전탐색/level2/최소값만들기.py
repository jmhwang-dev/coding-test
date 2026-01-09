# greedy
def solution(A,B):
    answer = 0
    
    sorted_a = sorted(A)
    sorted_b = sorted(B, reverse=True)
    
    for a, b in zip(sorted_a, sorted_b):
        answer += a*b

    return answer