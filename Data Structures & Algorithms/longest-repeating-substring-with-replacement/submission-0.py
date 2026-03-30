class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        largest, left, maxf = 0,0,0

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            maxf = max(maxf, count[s[right]])
            while (right-left+1)-maxf > k:
                count[s[left]]-=1
                left+=1
            largest = max(largest, right-left+1)
        return largest