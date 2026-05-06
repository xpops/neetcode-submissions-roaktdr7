class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 이게 바이너리서치라고?
        # 그냥 가능한 value들을 array로 나열하고 다 해보는 대신에 binary search로 해보기.
        # ***Value들간의 크기 상관관계가 순서대로 있기 때문에 가능한 듯?***

        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = int((l + r) / 2)
            # verify k
            hCurr = 0
            for pile in piles:
                hCurr += math.ceil(pile / k)
            if hCurr <= h: # k equal or too large
                res = k # 더 작은 k가 가능할 수도 있으니까 일단 저장하고 계속 루프
                r = k - 1
            else: #k too small
                l = k + 1
                k += 1 # !여기가 포인트! minimum k를 구하는 거니까 작은채로 끝날때 1 올려줘야함.
        
        return k