class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashedNums = set(nums)

        sequences = []
        for i in range(len(nums)):
            currentNum = nums[i]
            if currentNum-1 not in hashedNums:
        
                currentSequence = [currentNum]
                for i in range(len(nums)):
                    if currentNum+1 in hashedNums:
                        currentSequence.append(currentNum+1)
                        currentNum += 1
                sequences.append(currentSequence)

        maxSequence = []
        for s in sequences:
            if len(s) > len(maxSequence):
                maxSequence = s

        print(sequences)
        return len(maxSequence)