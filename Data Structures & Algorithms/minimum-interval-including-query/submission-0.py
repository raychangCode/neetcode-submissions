class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        min_heap = []
        ans = {}
        idx = 0

        for q in sorted(queries):
            while idx < len(intervals) and intervals[idx][0] <= q:
                left, right = intervals[idx]
                heapq.heappush(min_heap, (right - left + 1, right))
                idx += 1

            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)

            if min_heap:
                ans[q] = min_heap[0][0]
            else:
                ans[q] = -1

        return [ans[q] for q in queries]