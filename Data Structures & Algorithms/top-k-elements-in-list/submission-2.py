class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # create dict
        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1
        sorted_count = sorted(count, key=count.get, reverse=True)
        print(count)
        # return
        return sorted_count[:k]