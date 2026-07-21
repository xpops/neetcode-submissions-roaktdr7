class Solution: # O(n(nodes) * m(edges))
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        connected = set()

        def dfs(node):
            if node in connected:
                return
            
            connected.add(node)
            
            for edge in edges:
                if edge[0] == node:
                    dfs(edge[1])
                elif edge[1] == node:
                    dfs(edge[0])
        
        dfs(0)
        
        if len(connected) != n:
            return False
        
        return True