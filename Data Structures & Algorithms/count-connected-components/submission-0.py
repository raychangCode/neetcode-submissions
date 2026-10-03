class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        memo = set()
        count = 0

        def dfs(node):
            
            for nei in graph[node]:
                if nei not in memo:
                    memo.add(nei)
                    dfs(nei)

        for node in range(n):
            if node not in memo:
                memo.add(node)
                dfs(node)
                count += 1

        return count