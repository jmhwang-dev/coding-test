class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) == 1:
            if citations[0] > 0:
                return 1
            return 0
        
        max_cit = max(citations)
        for i in range(max_cit, -1, -1):
            tmp = list(map(lambda x: x-i, citations))
            cnt = len(list(filter(lambda x: x >= 0, tmp)))
            if i <= cnt:
                return i