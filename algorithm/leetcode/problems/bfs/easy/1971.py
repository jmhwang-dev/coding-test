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


# again
from collections import deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        if source == destination:
            return True

        adj = collections.defaultdict(list)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = {source}
        queue = deque([source])

        while queue:
            node = queue.popleft()
            if node == destination:
                return True

            for adj_node in adj[node]:
                if adj_node not in visited:
                    visited.add(adj_node)
                    queue.append(adj_node)
        return False
                