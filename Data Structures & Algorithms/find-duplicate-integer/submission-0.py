class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # value is between 1 - n
        # so we can flip the sign of the value and its corresponding idx
        # if a value is neg, then that's it
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                return abs(num)
            nums[idx] *= -1
        return -1