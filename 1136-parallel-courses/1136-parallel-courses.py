class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        
        g = defaultdict(list)
        degree = [0 for _ in range(n+1)]
        
        for u, v in relations:
            g[u].append(v)
            degree[v] += 1
        
        q = deque([i for i in range(1, n+1) if degree[i] == 0])
        sems, courses = 0, 0
        while q:
            sems += 1
            length = len(q)
            for _ in range(length):
                u = q.popleft()
                courses += 1
                for v in g[u]:
                    degree[v] -= 1
                    if degree[v] == 0:
                        q.append(v)

        if courses == n:
            return sems
        else:
            return -1