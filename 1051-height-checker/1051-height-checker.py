class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ans = 0
        sortedHeights = sorted(heights)
        for i in range(len(heights)):
            if sortedHeights[i] != heights[i]:
                ans += 1
        return ans