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
            
            res = True
            for pre in preMap[crs]:
                if not dfs(pre):
                    res = False
            
            if res:
                preMap[crs] = []
            
            visited.remove(crs)
            
            return res
        
        res = True
        for crs in range(numCourses):
            if not dfs(crs):
                res = False
        return res