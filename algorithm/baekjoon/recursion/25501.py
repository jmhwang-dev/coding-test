# 입력
# 첫째 줄에 테스트케이스의 개수 T가 주어진다. (1 <= T <= 1000)

# 둘째 줄부터 
# T개의 줄에 알파벳 대문자로 구성된 문자열 S가 주어진다. (1 <= |S| <= 1000)

# 출력
# 각 테스트케이스마다, isPalindrome 함수의 반환값과 recursion 함수의 호출 횟수를 한 줄에 공백으로 구분하여 출력한다.

# N = 5
# T = ["AAA","ABBA","ABABA","ABCA","PALINDROME"]

N = int(input())
T = []
for i in range(N):
    T.append(str(input()))

count = 0
def recursion(s: str, l: int, r: int):
    global count
    count += 1 
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l+1, r-1)

def isPalindrom(s: str):
    global count
    count = 0
    return recursion(s, 0, len(s)-1)

def solution(S):
    return isPalindrom(S)

for i, S in enumerate(T):
    print(solution(S), count)