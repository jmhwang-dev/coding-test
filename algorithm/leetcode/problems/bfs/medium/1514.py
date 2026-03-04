# Dijkstra

import collections
import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        graph = collections.defaultdict(list)
        for i in range(len(succProb)):
            start, end = edges[i]
            # max heap, minus
            graph[start].append([-succProb[i], end])
            graph[end].append([-succProb[i], start])

        max_prob = [0.0] * n
        max_prob[start_node] = 1.0
        pq = [[-1.0, start_node]]

        while pq:
            curr_prob, curr_node = heapq.heappop(pq)
            real_prob = -curr_prob

            if real_prob < max_prob[curr_node]:
                continue
            
            if curr_node == end_node:
                return real_prob

            for adj_prob, adj_node in graph[curr_node]:
                new_prob = curr_prob * adj_prob  # minus, minus -> max heap

                if new_prob > max_prob[adj_node]:
                    max_prob[adj_node] = new_prob
                    heapq.heappush(pq, [-new_prob, adj_node])
                        
                # print(max_prob, curr_node, adj_node)
        return max_prob[end_node]