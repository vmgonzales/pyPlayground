class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelSet = set()
        ans = 0
        
        for jewel in jewels:
            jewelSet.add(jewel)
        #print(jewelSet)
        
        for stone in stones:
            if stone in jewelSet:
                ans += 1
        
        return ans