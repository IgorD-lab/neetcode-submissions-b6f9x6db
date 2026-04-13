class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_count = 0

        # set iteration
        for num in num_set:
            # go in only if you are at the smallest number of a consecutive streak
            if num - 1 not in num_set:
                curr_num = num
                count = 1
                # as loong as there is a bigger number in the current streak keep going
                while curr_num + 1 in num_set:
                    count += 1
                    curr_num += 1
                # if the streak you just iterated trough is the largest so far set max_count to that
                if count > max_count:
                    max_count = count

        return max_count 

        

                