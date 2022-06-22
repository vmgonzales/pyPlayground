class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        # Start with the sum of all 1 length arrays
        ans = sum(arr)
        
        for j in range(3, len(arr) + 1, 2):
            for i in range(len(arr)):
                if (i+j) > len(arr): break
                ans += sum(arr[i: i+j])
        return ans