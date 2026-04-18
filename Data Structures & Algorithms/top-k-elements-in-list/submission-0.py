class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = Counter(nums).most_common()
        out = []
        for i in range(k):
            out.append(num_count[i][0])
        
        return out