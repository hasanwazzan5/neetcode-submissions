class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = set(nums)
        for i in range(len(nums)):
            #hashmap[nums[i]] = target - nums[i]
            diff = target - nums[i]

            tempNums = nums.copy()
            tempNums[i] = None
            
            if diff in tempNums:

                return [i, tempNums.index(diff)]

