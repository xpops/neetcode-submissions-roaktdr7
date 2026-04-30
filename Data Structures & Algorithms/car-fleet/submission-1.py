class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create sorted array of [p, s]
        arr = [[p, s] for p, s in zip(position, speed)]
        arr.sort(key=lambda x: x[0], reverse=True) # p 기준으로 sort

        stack = []

        # loop
        for i, car in enumerate(arr):
            if not stack or stack[-1][1] > car[1] or (target - stack[-1][0]) / stack[-1][1] < (target - car[0]) / car[1]:
                stack.append(car)
        
        return len(stack)