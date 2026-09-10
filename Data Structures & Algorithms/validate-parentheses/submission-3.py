class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s) == 1):
            return False
        stack = []
        d = {'[' : ']', '{' : '}', '(' : ')'}
        for c in s:
            if c in d:
                stack.append(c)
            elif len(stack) == 0 or d[stack[-1]] != c:
                return False
            else:
                stack.pop()
        return len(stack) == 0