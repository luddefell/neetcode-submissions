class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_hist = {}
        t_hist = {}
        for char in s:
            if char not in s_hist:
                s_hist[char] = 1
            else:
                s_hist[char] = s_hist[char] + 1
        for char in t:
            if char not in t_hist:
                t_hist[char] = 1
            else:
                t_hist[char] = t_hist[char] + 1
        return t_hist == s_hist
        # l = 0
        # r = len(s) - 1
