class Solution:
    def countBits(self, n: int) -> List[int]:
        # offset is the most significant bit so far, the curr highest power of 2
        # dp[n] = 1 + dp[n - offset]

        dp = [0] * (n + 1)
        sub = 1

        for i in range(1, n + 1):
            if sub * 2 == i: # 
                sub = i
            dp[i] = 1 + dp[i - sub]

        return dp

