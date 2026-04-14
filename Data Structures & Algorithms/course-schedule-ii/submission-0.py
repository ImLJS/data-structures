from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited, cycle = set(), set()
        graph = defaultdict(list)
        res = []

        for u, v in prerequisites:
            graph[u].append(v)
        
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True

            cycle.add(course)

            for neighbour in graph[course]:
                if not dfs(neighbour):
                    return False

            cycle.remove(course)
            visited.add(course)
            res.append(course)
            return True 
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res