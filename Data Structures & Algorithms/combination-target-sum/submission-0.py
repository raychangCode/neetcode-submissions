class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()

        def dfs(idx, curr, total):
            if total == target:
                ans.append(curr.copy())
                return

            for i in range(idx, len(nums)):
                if total + nums[i] > target:
                    return
                curr.append(nums[i])
                dfs(i, curr, total + nums[i])
                curr.pop()

        dfs(0, [], 0)
        return ans