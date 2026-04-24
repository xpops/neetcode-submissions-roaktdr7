class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(n)이니까 Sorting은 아님.
        # Hashmap?
        # key: num, value: consecutive sequence starting from num

        # failed approach:
        # consec_seq_map = dict.fromkeys(nums, 1)
        # for i in range(1, len(nums)):
        #     consec_seq_map[nums[i] - 1] += 1

        num_set = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in num_set: # num is a start
                count = 1
                while num + count in num_set:
                    count += 1
                if longest < count:
                    longest = count
        
        return longest