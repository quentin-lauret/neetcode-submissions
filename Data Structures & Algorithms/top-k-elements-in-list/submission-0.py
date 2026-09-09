class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {num: 0 for num in set(nums)}
        for num in nums:
            d[num] += 1
        sorted_list = sorted(list(d.items()), key=lambda x: x[1], reverse=True)
        return [x[0] for x in sorted_list[:k]]