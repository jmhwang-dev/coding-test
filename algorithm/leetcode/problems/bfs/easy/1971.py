from collections import deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        if source == destination:
            return True

        adj = collections.defaultdict(set)

        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
        
        if source not in adj:
            return False
        
        queue = deque(adj[source])
        visited = {source}

        while queue:
            curr_node = queue.popleft()
            
            if curr_node == destination:
                return True

            for node in adj[curr_node]:
                if node not in visited:
                    visited.add(node)
                    queue.append(node)
        return False