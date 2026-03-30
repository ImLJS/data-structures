class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda inter: inter[0])
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            
            else:
                inter = [merged[-1][0], max(merged[-1][1], interval[1])]
                merged[-1] = inter
        return merged