class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_s = sorted(nums)
        l = []
        for i in range(len(nums_s)):
            k = i + 1
            j = len(nums_s) - 1
            target = -nums_s[i]
            counted = 0
            while k < j:
                if k == i:
                    k += 1
                if j == i:
                    j -= 1
                if nums_s[k] + nums_s[j] > target:
                    j -= 1
                elif nums_s[k] + nums_s[j] < target:
                    k += 1
                else:
                    l.append((nums_s[i], nums_s[j], nums_s[k]))
                    k += 1
                    j -= 1
        return list(set(l))
            