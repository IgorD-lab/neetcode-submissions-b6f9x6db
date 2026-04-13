class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_s = set()
        maxS = 0
        l, r = 0, 0
        
        while r < len(s):
            while s[r] in curr_s:
                    curr_s.remove(s[l])
                    l += 1
            curr_s.add(s[r])    
            maxS = max(maxS, len(curr_s))
            
            r += 1
        return maxS