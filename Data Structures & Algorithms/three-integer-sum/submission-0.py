class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        for start in range(len(nums)-2):
            if nums[start] > 0:
                break
            
            if start > 0 and nums[start] == nums[start-1]:
                continue

            left, right = start + 1, len(nums)-1

            while left<right:
                total = nums[start] + nums[left] + nums[right]

                if not total:
                    res.add((nums[start], nums[left], nums[right]))
                
                if total>0:
                    right-=1
                else:
                    left+=1
        
        return list(res)