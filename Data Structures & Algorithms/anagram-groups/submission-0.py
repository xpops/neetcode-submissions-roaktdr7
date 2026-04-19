class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            str_map[sortedS].append(s)
        
        return list(str_map.values())