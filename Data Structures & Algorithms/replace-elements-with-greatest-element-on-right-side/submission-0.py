class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        
        for i in range(len(arr)-1):
            sliced_arr = arr[i+1:]
            max_num = max(sliced_arr)
            arr[i] = max_num
        arr[-1] = -1
        return arr