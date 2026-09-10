class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[l] > nums[m]:
                r = m
            elif nums[r] < nums[m]:
                l = m + 1
            elif nums[l] < nums[r]:
                return nums[l]
            elif nums[r] == nums[m] or nums[l] == nums[m]:
                return nums[m]
        return nums[r]