from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)

        for char in strs:
            word = "".join(sorted(char))
            freq[word].append(char)

        return list(freq.values())