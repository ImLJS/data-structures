class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        L = 0
        R = len(nums)-1

        while L<R:
            cur_sum = nums[L]+nums[R]

            if cur_sum == target:
                return [L+1,R+1]
            
            elif cur_sum > target:
                R-=1
            else:
                L+=1
        
