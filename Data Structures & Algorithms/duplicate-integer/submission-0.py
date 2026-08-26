class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cashe = dict()
        for num in nums:
            if num in cashe:
                return True
            else:
                cashe[num] = 1
        return False