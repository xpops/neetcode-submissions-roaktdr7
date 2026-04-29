class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                removed = stack.pop()
                result[removed[1]] = i - removed[1]
            stack.append([t, i])
            print(stack, result)
        return result
        