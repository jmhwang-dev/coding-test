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