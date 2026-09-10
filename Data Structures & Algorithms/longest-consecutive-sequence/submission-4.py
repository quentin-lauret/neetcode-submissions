class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nb_cons_max = 0
        possible_start = set(nums)
        for i in range(len(nums)):
            if nums[i] - 1 in possible_start:
                continue
            last = nums[i]
            nb_cons = 1
            while last + 1 in possible_start:
                last += 1
                nb_cons += 1
            nb_cons_max = max(nb_cons, nb_cons_max)
        return nb_cons_max