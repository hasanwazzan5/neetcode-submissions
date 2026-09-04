class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = ['{','[','(']
        closing = ['}',']',')']

        for i in range(len(s)):
            if s[i] in opening:
                stack.append(s[i])
            elif s[i] in closing:
                if len(stack) == 0:
                    return False
                elif stack[-1] == opening[closing.index(s[i])]:
                    stack.pop()
                else:
                    return False

        if len(stack) != 0:
            return False
        else:
            return True
