def cantor_set(line, start, end):
    if end - start < 3:
        return

    whitespace = (end-start) // 3
    for i in range(start+whitespace, end-whitespace):
        line[i] = ' '
    
    cantor_set(line, start, start+whitespace)
    cantor_set(line, end-whitespace, end)

def solution(N=3):
    line = '-' * 3**N
    line = list(line)
    cantor_set(line, 0, len(line))
    print(''.join(line))

while True:
    try:
        N = int(input())
        solution(N)
    except:
        break