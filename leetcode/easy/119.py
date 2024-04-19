# 2: append 제외
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for _ in range(rowIndex):
            row = [1] + [row[i] + row[i+1] for i in range(len(row)-1)] + [1]
        return row


# 1
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [[1]] # 0
        ans.append([1,1]) # 1
        if rowIndex < 2:
            return ans[rowIndex]
        for i in range(rowIndex - 1):
            index = 0
            output = []
            target = ans[-1]
            while index+1 < len(target):
                output.append(sum(target[index:index+2]))
                index += 1 
            result = [1] + output + [1]
            ans.append(result)
        return ans[rowIndex]