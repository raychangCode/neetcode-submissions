class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis_map = defaultdict(list)
        ans = []
        for p1, p2 in points: 
            dis_map[p1**2 + p2**2].append([p1, p2])

        dist = []
        for key in dis_map:
            dist.append(key)
        dist.sort()

        for d in dist:
            for p in dis_map[d]:
                if len(ans) < k:
                    ans.append(p)
                if len(ans) == k:
                    return ans
