class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Array -> Linked List 변환
        # array = [3, 1, 3, 4, 2]
        # linkedlist = 0 -> 3 -> 4 -> 2  (인덱스가 value, 값이 next)
        #                   ^ㄴㅡㅡㅡㅡㅡ⅃
        # array에 0이 없을 때만 가능. 루프에 속하지 않는 노드가 적어도 하나는 있어야 함
        # 안 그러면 전체가 circular 루프에 속하고 시작점이 없어지니까

        # Floyd로 첫번째 만나는 지점 찾기 (루프 안에서 만남)
        s, f = 0, 0
        while True:
            s = nums[s] # move 1
            f = nums[nums[f]] # move 2
            if s == f:
                break
        
        # 시작점과 floyd 지점에서부터 동시에 움직이면서 만나는 지점 찾기 (그 지점이 루프의 시작점)
        i, j = 0, s
        while i != j:
            i = nums[i]
            j = nums[j]
        
        return i