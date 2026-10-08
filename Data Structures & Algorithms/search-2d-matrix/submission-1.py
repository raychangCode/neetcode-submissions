class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in matrix:
            if row[-1] >= target:
                return self.b_search(row, target)
        return False

    def b_search(self, nums, target):
        n = len(nums)
        left = 0
        right = n - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False