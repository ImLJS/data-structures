class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        answer = Counter(s1)
        main = defaultdict(int)
        left = 0
        
        for right in range(len(s2)):
            main[s2[right]] = 1 + main.get(s2[right], 0)
            while right-left+1>len(s1):
                main[s2[left]]-=1
                if main[s2[left]] == 0:
                    del main[s2[left]]
                left+=1
            if main == answer:
                return True
        return False