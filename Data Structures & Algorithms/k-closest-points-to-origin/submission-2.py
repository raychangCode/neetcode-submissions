class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        ans = []

        for p1, p2 in points:
            dist = -(p1 ** 2 + p2 ** 2)
            heapq.heappush(heap, [dist, p1, p2])
            if len(heap) > k:
                heapq.heappop(heap)

        while heap:
            d, p1, p2 = heapq.heappop(heap)
            ans.append([p1, p2])
        return ans