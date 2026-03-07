# bfs

from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        queue = deque([(src, 0)])
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


# dijkstra
import collections
import heapq
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for s, d, p in flights:
            graph[s].append((d, p))

        visited_stops = [float('inf')] * n
        pq = [(0, src, 0)]

        while pq:
            curr_price, curr_node, curr_k = heapq.heappop(pq)

            if curr_node == dst:
                return curr_price

            if curr_k >= visited_stops[curr_node]:
                continue

            visited_stops[curr_node] = curr_k

            if curr_k <= k:
                for adj_to, price in graph[curr_node]:
                    new_price = curr_price + price
                    heapq.heappush(pq, (new_price, adj_to, curr_k + 1))

        return -1