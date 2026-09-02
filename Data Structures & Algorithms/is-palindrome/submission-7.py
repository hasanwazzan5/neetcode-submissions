class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = list(s)
        for char in s.copy():
            letterNum = ord(char) - ord('a')
            if letterNum < 0 or letterNum > 25:
                if char not in list('0123456789'):
                    s.remove(char)

        print(s, list('0123456789'))

        for i in range(len(s)):
            if len(s) <= 1:
                return True

            j = (len(s) - 1) - i

            if i>j:
                return True
            elif s[i] != s[j]:
                return False
        
        return True