class Solution: # Adjacency List: O(n + m)
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if len(edges) != n - 1:
            return False
        
        adjList = [[] for i in range(n)]
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        
        connected = set()
        def dfs(node):
            if node in connected:
                return
            
            connected.add(node)
            
            for neighbor in adjList[node]:
                dfs(neighbor)
        dfs(0)
        
        if len(connected) != n:
            return False
        
        return True