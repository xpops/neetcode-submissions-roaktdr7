"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # edge cases: empty graph
        if not node:
            return None

        visited = {} # old -> new

        def dfs(origNode):
            if origNode in visited:
                return visited[origNode]
            
            cNode = Node(origNode.val)
            visited[origNode] = cNode

            for origNeighbor in origNode.neighbors:
                cNode.neighbors.append(dfs(origNeighbor))
            
            return cNode
        
        return dfs(node)

        