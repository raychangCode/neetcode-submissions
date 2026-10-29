class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        def dfs(node, par):
            if node in visit:
                return False
            if node == par:
                return True

            visit.add(node)
            for nei in graph[node]:
                if dfs(nei, par):
                    return True
            return False
        
        for u, v in edges:
            visit = set()
            if dfs(u, v):
                return [u, v]
            graph[u].append(v)
            graph[v].append(u)
        return []