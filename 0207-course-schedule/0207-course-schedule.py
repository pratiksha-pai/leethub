class Solution:
    def canFinish(self, num_courses: int, prereq: List[List[int]]) -> bool:
        
        graph = [[] for _ in range(num_courses)]
        visited = [0 for _ in range(num_courses)]
        
        for i in range(len(prereq)):
            [a, b] = prereq[i]
            graph[b].append(a)
            
        def dfs(node):
            
            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return True  # kinda caching, since we dont check the route of already traversed node
            
            visited[node] = 1
            for neigh in graph[node]:
                if not dfs(neigh):
                    return False
            
            visited[node] = 2
            return True
        
        for i in range(num_courses):
            if not dfs(i):
                return False
        
        return True