from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        graph = defaultdict(list)

        for u, v in prerequisites:
            graph[u].append(v)
        
        def dfs(course):
            if not graph[course]:
                return True

            if course in visited:
                return False

            visited.add(course)

            for neighbour in graph[course]:
                if not dfs(neighbour):
                    return False

            graph[course] = []
            return True 
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True