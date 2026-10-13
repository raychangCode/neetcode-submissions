class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}

        def dfs(idx, curr):
            if idx == n:
                if curr == target:
                    return 1
                else:
                    return 0
            if (idx, curr) in memo:
                return memo[(idx, curr)]
            memo[(idx, curr)] = dfs(idx + 1, curr + nums[idx]) + dfs(idx + 1, curr - nums[idx])
            

            return memo[(idx, curr)]
        
        return dfs(0, 0)


