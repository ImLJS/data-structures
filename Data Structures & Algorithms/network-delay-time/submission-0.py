import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,time in times:
            graph[u].append((v,time)) # (node, time taken)
        
        min_times = {}
        min_heap = [(k, 0)]

        while min_heap:
            node, time = heapq.heappop(min_heap)

            if node in min_times:
                continue
            
            min_times[node] = time

            for neighbour, neighbour_time in graph[node]:
                if neighbour not in min_times:
                    heapq.heappush(min_heap, (neighbour, neighbour_time + time))
            
        if len(min_times) == n:
            return max(min_times.values())
        else:
            return -1
            


