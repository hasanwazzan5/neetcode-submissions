class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for i in range(len(nums)):

            j, k = i+1, len(nums)-1
            while j < k:
                if j == i:
                    j += 1
                    continue
                if k == i:
                    k -= 1
                    continue

                if -nums[i] > nums[j] + nums[k]:
                    j += 1
                    continue
                elif -nums[i] < nums[j] + nums[k]:
                    k -= 1
                    continue
                elif -nums[i] == nums[j] + nums[k]:
                    if [nums[i], nums[j], nums[k]] not in output:
                        output.append([nums[i], nums[j], nums[k]])
                
                j = j+1

        return output