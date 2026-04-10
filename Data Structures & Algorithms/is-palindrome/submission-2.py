class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""

        for char in s:
            if char.isalnum():
                word+=char.lower()

        return word == word[::-1]