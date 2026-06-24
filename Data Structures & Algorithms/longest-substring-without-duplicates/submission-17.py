class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxx = 0
        seen = defaultdict(int)
        for i in range(len(s)):
            seen[s[i]] += 1
            while seen[s[i]] > 1:
                seen[s[l]] -= 1
                l += 1

            maxx = max(maxx, i - l + 1)
        return maxx
            