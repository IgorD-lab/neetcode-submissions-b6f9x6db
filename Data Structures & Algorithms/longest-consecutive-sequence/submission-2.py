class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        longest = [] # track numbers for debugging
        counter = 1
        max_count = 1
        # edge case with empty list
        if len(nums) < 1:
            max_count = 0
        for i in range(len(nums)):
            if nums[i] in longest:
                pass
            elif nums[i] - 1 == nums[i - 1]:
                longest.append(nums[i])
                counter += 1
                if counter > max_count:
                    max_count = counter
            else:
                longest = [nums[i]]
                counter = 1
        return max_count

        

                