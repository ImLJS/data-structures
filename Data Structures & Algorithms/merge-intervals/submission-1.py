class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda inter: inter[0])
        window = []

        for x, y in intervals:
            print(x, y)
            if window and window[-1][1] >= x:
                pop_x, pop_y = window.pop()
                interval = [pop_x, max(pop_y, y)]
                window.append(interval)
            else:
                window.append([x,y])
        return window