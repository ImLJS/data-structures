class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(arr, left, right):
            if right-left+1 <= 1:
                return arr
            
            mid = (left+right)//2
            mergeSort(arr, left, mid)
            mergeSort(arr, mid+1, right)

            merge(arr, left, mid, right)

            return arr
        
        def merge(arr, left, mid, right):
            L = arr[left:mid+1]
            R = arr[mid+1:right+1]

            i, j, k = 0, 0, left

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i+=1
                else:
                    arr[k] = R[j]
                    j+=1
                k+=1
            
            while i < len(L):
                arr[k] = L[i]
                i+=1
                k+=1
            while j < len(R):
                arr[k] = R[j]
                k+=1
                j+=1
        
        return mergeSort(nums, 0, len(nums)-1)



