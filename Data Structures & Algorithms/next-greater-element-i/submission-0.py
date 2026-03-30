class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1]*len(nums2)
        stack = []
        ans = [-1]*len(nums1)

        for index, val in enumerate(nums2):
            while stack and nums2[stack[-1]]<val:
                res[stack.pop()] = val
            stack.append(index)
        
        for i in range(len(nums1)):
            index = nums2.index(nums1[i])
            ans[i] = res[index]

        return ans 