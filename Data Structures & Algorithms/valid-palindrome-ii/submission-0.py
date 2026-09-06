class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left<right:
            if s[left] != s[right]:
                leftCheck = s[left+1:right+1] == s[left+1:right+1][::-1]
                rightCheck = s[left:right] == s[left:right][::-1]
                return leftCheck or rightCheck
            left+=1
            right-=1
        
        return True