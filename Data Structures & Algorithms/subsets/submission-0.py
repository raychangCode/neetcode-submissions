class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def helper(idx, subset):

            if idx >= len(nums):
                ans.append(subset.copy())
                return

            subset.append(nums[idx])
            helper(idx + 1, subset)
            subset.pop()
            helper(idx + 1, subset)

        helper(0, [])
        return ans