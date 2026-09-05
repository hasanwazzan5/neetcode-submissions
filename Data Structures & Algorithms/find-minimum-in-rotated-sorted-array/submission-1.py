class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1

        while True:
            if nums[start] <= nums[end]:
                return nums[start]

            mid = (start + end) // 2
            print(start, mid, end)

            if nums[start] < nums[mid]:
                start = mid+1

            elif nums[start] > nums[mid]:
                end = mid

            elif nums[mid] < nums[end]:
                end = mid-1
            
            elif nums[mid] > nums[end]:
                start = mid+1




