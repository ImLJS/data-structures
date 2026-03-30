class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for char in details:
            age = char[-4]+char[-3]
            if int(age)>60:
                count+=1
        return count