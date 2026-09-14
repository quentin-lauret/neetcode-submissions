class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l + 1 < r:
            m = (l + r) // 2
            if target >= nums[l] and target <= nums[m]:
                r = m
            elif target >= nums[m] and target <= nums[r]:
                l = m
            elif nums[l] >= nums[m]:
                r = m
            elif nums[r] <= nums[m]:
                l = m
            else:
                return -1
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        return -1