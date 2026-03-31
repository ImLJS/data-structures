class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note = Counter(ransomNote)

        for char in magazine:
            if not note:
                return True
            
            if char in note:
                if note[char] > 0:
                    note[char] -= 1
                    if note[char] == 0:
                        del note[char]
        
        return not note