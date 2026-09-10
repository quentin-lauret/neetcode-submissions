class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_l = []
        l_r = []
        m_l = 1
        m_r = 1
        for i in range(len(nums)):
            m_l *= nums[i]
            m_r *= nums[-i - 1]
            l_l.append(m_l)
            l_r.append(m_r)
        l_r = l_r[::-1]
        l = []
        for i in range(len(nums)):
            p = 1
            if i != len(nums) - 1:
                p *= l_r[i + 1]
            if i != 0:
                p *= l_l[i - 1]
            l.append(p)
        return l