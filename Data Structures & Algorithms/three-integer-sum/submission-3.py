class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for start in range(len(nums)-2):
            if nums[start]>0:
                break
            
            if start > 0 and nums[start-1] == nums[start]:
                continue
            
            left = start+1
            right = len(nums)-1

            while left<right:
                total = nums[left] + nums[right] + nums[start]

                if not total:
                    ans.append([nums[start], nums[left], nums[right]])
                    left+=1
                    right-=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
                
                elif total > 0:
                    right-=1
                else:
                    left+=1
        return ans
            
            