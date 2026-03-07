from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        queue = deque([(src, 0)])
        # prices[i]는 i 노드까지 오는 최소 비용
        prices = [float('inf')] * n
        prices[src] = 0

        stops = 0
        while queue and stops <= k:
            for _ in range(len(queue)):
                curr_node, curr_price = queue.popleft()

                for neighbor, price in graph[curr_node]:
                    new_price = curr_price + price
                    
                    if new_price < prices[neighbor]:
                        prices[neighbor] = new_price
                        queue.append((neighbor, new_price))
            stops += 1

        return prices[dst] if prices[dst] != float('inf') else -1