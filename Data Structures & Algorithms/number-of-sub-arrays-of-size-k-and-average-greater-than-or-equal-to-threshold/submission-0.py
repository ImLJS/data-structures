class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        total = k*threshold

        cur_sum = sum(arr[:k])
        if cur_sum >= total:
            res+=1
        
        for i in range(k, len(arr)):
            cur_sum -= arr[i-k]
            cur_sum += arr[i]
            if cur_sum >= total:
                res+=1
        
        return res