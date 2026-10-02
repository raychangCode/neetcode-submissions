class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        min_heap = [(0, k)] # heap takes the first ele to sort
        visited = set()
        ans = 0

        while min_heap:
            w1, n1 = heapq.heappop(min_heap)

            if n1 in visited:
                continue

            visited.add(n1)
            ans = max(ans, w1)

            for n2, w2 in graph[n1]:
                if n2 not in visited:
                    heapq.heappush(min_heap, (w1 + w2, n2))

        if len(visited) == n:
            return ans
        return -1