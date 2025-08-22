class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        if numRows == 1:
            return ans
        ans.append([1,1])
        if numRows == 2:
            return ans

        for i in range(numRows):
            if i < 2:
                continue
            index = 0
            pascal = []
            while index + 1 < i:
                pascal.append(sum(ans[-1][index:index+2]))
                index += 1
            
            result = [1] + pascal + [1]
            ans.append(result)
        return ans