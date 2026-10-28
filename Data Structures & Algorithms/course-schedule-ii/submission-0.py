class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = { c : [] for c in range(numCourses)}

        for c, pre in prerequisites:
            graph[c].append(pre)

        ans = []
        seen = set()
        cycle = set()

        def dfs(node):
            if node in cycle:
                return False

            if node in seen:
                return True

            cycle.add(node)
            for pre in graph[node]:
                if dfs(pre) == False:
                    return False

            cycle.remove(node)
            seen.add(node)
            ans.append(node)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return ans