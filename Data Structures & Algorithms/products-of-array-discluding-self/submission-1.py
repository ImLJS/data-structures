class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        prefix = deque([])
        postfix = deque([])
        res = []

        total = 1
        for n in nums:
            total*=n
            prefix.append(total)
        total = 1
        for i in range(len(nums)-1, -1, -1):
            total*=nums[i]
            postfix.appendleft(total)
        for i in range(len(nums)):
            L = prefix[i-1] if i>0 else 1
            R = postfix[i+1] if i<len(nums)-1 else 1
            res.append(L*R)
        
        return res

