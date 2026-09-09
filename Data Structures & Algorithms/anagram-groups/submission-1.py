class Solution:
    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {str(sorted(s)):[] for s in set(strs)}
        for i in range(len(strs)):
            sorted_i = str(sorted(strs[i]))
            d[sorted_i].append(strs[i])
        return list(d.values())

