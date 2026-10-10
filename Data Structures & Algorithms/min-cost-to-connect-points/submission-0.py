class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        graph = defaultdict(list)

        for i in range(N):
            for j in range(i + 1, N):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                graph[i].append([dist, j])
                graph[j].append([dist, i])

        ans = 0
        visit = set()
        heap = [(0, 0)]

        while len(visit) < N:
            cost, idx = heapq.heappop(heap)
            if idx in visit:
                continue
            ans += cost
            visit.add(idx)
            for nei_cost, nei in graph[idx]:
                if nei not in visit:
                    heapq.heappush(heap, (nei_cost, nei))

        return ans
        