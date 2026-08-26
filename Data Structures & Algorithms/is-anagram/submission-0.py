class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = list(s)
        list_t = list(t)

        list_s.sort()
        list_t.sort()

        new_s = "".join(list_s)
        new_t = "".join(list_t)

        return new_s == new_t