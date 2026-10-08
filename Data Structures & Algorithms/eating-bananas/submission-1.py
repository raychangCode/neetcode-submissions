class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = right

        while left <= right:
            k = left + (right - left) // 2
            
            time = 0
            for p in piles:
                time += math.ceil(p / k)

            if time <= h:
                ans = k
                right = k - 1
            else:
                left = k + 1

        return ans