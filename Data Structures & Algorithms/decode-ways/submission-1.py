class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {len(s): 1}

        def dfs(i):
            if i in memo:
                return memo[i]

            if s[i] =='0':
                return 0

            ans = dfs(i + 1)
            if i < len(s) - 1:
                if (s[i] == '1' or (s[i] == '2' and s[i+1] <= '6')):
                    ans += dfs(i + 2)
            memo[i] = ans
            return ans

        return dfs(0)