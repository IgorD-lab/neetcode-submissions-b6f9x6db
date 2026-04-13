class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = ''.join(sorted(s1))
        l, r = 0, len(s1) - 1

        while r < len(s2):
            window = ''
            for i in range(l, r + 1):
                window = ''.join(s2[i]) + window
            window = ''.join(sorted(window))
            r += 1
            l += 1
            if window == s1:
                return True
        return False

# removing double sort would improve time but is cancer to implement