class Solution: # Sorted니까 양끝에서 시작해서 합이 target보다 크면 오른쪽애 빼고, 작으면 왼쪽애 빼고
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                break
        
        return [i + 1, j + 1]