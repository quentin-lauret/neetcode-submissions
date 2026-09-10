class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s) - 1
        while i < j:
            while i < len(s) and not ((s[i] >= 'a' and s[i] <= 'z') or (s[i] >= '0' and s[i] <= '9')):
                i += 1
            while j >= 0 and not ((s[j] >= 'a' and s[j] <= 'z') or (s[j] >= '0' and s[j] <= '9')):
                j -= 1
            if i < len(s) and j >= 0 and (s[i] != s[j]):
                return False
            i += 1
            j -= 1
        return i >= j
            