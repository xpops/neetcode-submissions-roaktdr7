class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        # track visited
        visited = set()
        
        rows, cols = len(heights), len(heights[0])
        res = []
        
        def pacific(r, c) -> bool: # can flow to pacific
            if r == 0 or c == 0:
                return True
            
            visited.add((r, c))
            curHeight = heights[r][c]
            
            neighbors = [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]

            for neighbor in neighbors:
                if neighbor[0] < 0 or neighbor[0] >= rows or neighbor[1] < 0 or neighbor[1] >= cols or (neighbor[0], neighbor[1]) in visited:
                    continue
                if heights[neighbor[0]][neighbor[1]] <= curHeight: # can flow
                    if pacific(neighbor[0], neighbor[1]):
                        return True
            
            return False

        def atlantic(r, c) -> bool: # can flow to atlantic
            if r == rows - 1 or c == cols - 1:
                return True
                        
            visited.add((r, c))
            curHeight = heights[r][c]
            
            neighbors = [[r - 1, c], [r + 1, c], [r, c - 1], [r, c + 1]]

            for neighbor in neighbors:
                if neighbor[0] < 0 or neighbor[0] >= rows or neighbor[1] < 0 or neighbor[1] >= cols or (neighbor[0], neighbor[1]) in visited:
                    continue
                if heights[neighbor[0]][neighbor[1]] <= curHeight: # can flow
                    if atlantic(neighbor[0], neighbor[1]):
                        return True
            
            return False
        
        for r in range(rows):
            for c in range(cols):
                pac = pacific(r, c)
                visited.clear()
                atl = atlantic(r, c)
                visited.clear()

                if pac and atl:
                    res.append([r, c])
    
        return res