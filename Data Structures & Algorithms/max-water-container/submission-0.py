class Solution:
    def amount_water(self, heights, l, r):
        return (r - l) * min(heights[l], heights[r])
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        m = -1
        while l < r:
            m = max(self.amount_water(heights, l, r), m)
            if (heights[l] < heights[r]):
                l += 1
            elif (heights[r] < heights[l]):
                r -= 1
            else:
                l += 1
                r -= 1
        return m