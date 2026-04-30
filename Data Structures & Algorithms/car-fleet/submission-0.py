class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create sorted array of [p, s]
        arr = [[p, s] for p, s in zip(position, speed)]
        arr.sort(key=lambda x: x[0]) # p 기준으로 sort

        # initialize var
        fleet = 1

        # loop
        i, j = len(arr) - 1, len(arr) - 2
        while i > -1 and j > -1:
            j = i - 1
            while j > -1:
                pi, pj = arr[i][0], arr[j][0]
                si, sj = arr[i][1], arr[j][1]
                if sj < si or (target - pi) / si < (target - pj) / sj: # i를 못따라잡음
                    fleet += 1
                    i = j
                    break
                j -= 1
        
        return fleet