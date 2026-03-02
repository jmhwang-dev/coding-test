# Dijkstra

import heapq
import collections

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        dist = {i: float('inf') for i in range(1, n + 1)}
        dist[k] = 0
        
        pq = [(0, k)]

        while pq:
            current_time, u = heapq.heappop(pq)
            
            if current_time > dist[u]:
                continue

            for v, w in graph[u]:
                new_time = current_time + w
                if new_time < dist[v]:
                    dist[v] = new_time
                    heapq.heappush(pq, (new_time, v))
                
        result = max(dist.values())
        return result if result != float('inf') else -1