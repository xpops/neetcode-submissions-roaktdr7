class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = defaultdict(int)
        for num in nums:
            count_map[num] += 1

        freq = [[] for _ in range(len(nums) + 1)]
        for key, value in count_map.items():
            freq[value].append(key)
        
        out = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                out.append(n)
                if len(out) == k:
                    return out