class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = []

        if amount == 0:
            return 0

        for n in range(amount + 1):
            if n == 0:
                memo.append(0)
                continue
            
            curMin = amount + 1

            for coin in coins:
                if n - coin < 0:
                    continue

                cur = memo[n - coin]
                if cur == -1:
                    continue
                
                cur += 1
                if cur < curMin:
                    curMin = cur

            if curMin == amount + 1:
                curMin = -1
    
            memo.append(curMin)
        
        return int(memo[-1])

