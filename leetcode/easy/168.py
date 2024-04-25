class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber > 0:
            columnNumber -= 1  # Excel은 1부터 시작하므로 1을 빼준다.
            remainder = columnNumber % 26
            result.append(chr(remainder + 65))  # ASCII 코드에서 65는 'A'
            columnNumber //= 26
        return ''.join(reversed(result))  # 결과 리스트를 거꾸로 조합하여 반환