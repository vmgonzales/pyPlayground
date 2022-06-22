class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        ones = [0] * len(arr)
        for i in range(len(arr)):
            copy = arr[i]
            ones[i] = 0
            while copy:
                ones[i] += copy % 2
                copy = copy // 2
        
        return([x for _, x in sorted(zip(ones, arr))])
        