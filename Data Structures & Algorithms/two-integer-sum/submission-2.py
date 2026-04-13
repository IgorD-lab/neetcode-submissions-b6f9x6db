class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}

        for i, value in enumerate(nums):
            wanted = target - value
            if wanted in temp:
                return [temp[wanted], i]
            else:
                temp[value] = i
        return
            
