class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for i in range(n)]
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        
        visited = set()
        count = 0

        def dfs(n):
            if n in visited:
                return
            
            visited.add(n)

            for neighbor in adjList[n]:
                dfs(neighbor)
            
        for i in range(n):
            if i in visited: # in already-scanned connected component
                continue
            dfs(i)
            count += 1
        
        return count
