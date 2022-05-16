class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums1)):
            index = nums2.index(nums1[i])
            answer.append(-1)
            j = index
            while answer[i] == -1 and j < len(nums2):
                if nums2[j] > nums1[i]:
                    answer[i] = nums2[j]
                j += 1
        return answer
            