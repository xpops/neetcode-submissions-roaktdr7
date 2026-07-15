class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visited = set()

        def dfs(crs):
            if crs in visited: # cycle
                return False
            if not preMap[crs]: # no prereq
                return True

            visited.add(crs)
            
            for pre in preMap[crs]:
                if not dfs(pre): # cycle detected
                    return False
            
            # this crs can be taken
            preMap[crs] = []
            visited.remove(crs)
            
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True