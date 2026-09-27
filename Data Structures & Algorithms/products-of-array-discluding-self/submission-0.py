class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # ans[i] = pre[i] x post[i]

        n = len(nums)
        pre = [0] * n
        post = [0] * n
        ans = [0] * n

        pre[0] = 1
        post[-1] = 1

        for i in range(1, n):
            pre[i] = nums[i-1] * pre[i - 1]

        for i in range(n - 2, -1, -1):
            post[i] = nums[i + 1] * post[i + 1]
 
        for i in range(n):
            ans[i] = pre[i] * post[i]

        return ans