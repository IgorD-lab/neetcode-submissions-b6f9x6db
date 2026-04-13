class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Solution 1:
        # sort lists and compare if they are the same
        #
        return sorted(s) == sorted(t)

        # Solution 2:
        # use counter to see if they are the same
        #
        return Counter(s) == Counter(t)

        # Solution 3:
        # manually compare number of each character with hash map
        #
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in counts:
            if countS[c] != countT.get(c, 0):
                return False
        