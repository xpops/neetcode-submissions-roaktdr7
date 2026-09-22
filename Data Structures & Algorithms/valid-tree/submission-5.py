class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool: 
        if len(edges) != n - 1:
            return False

        # Build adjacency list
        adj = [[] for _ in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        
        connected = set()
        
        def dfs(cur):
            if cur in connected:
                return
            connected.add(cur)
            for nex in adj[cur]:
                dfs(nex)
        
        dfs(0)
        
        return len(connected) == n
