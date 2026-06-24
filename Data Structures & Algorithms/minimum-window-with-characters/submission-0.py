class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hashmap = defaultdict(int)
        l = 0
        minn = 10000000000
        minn_str = ""
        for x in t:
            hashmap[x] += 1
        for i in range(len(s)):
            hashmap[s[i]] -= 1
            while all(value <= 0 for value in hashmap.values()):
                if i - l + 1 < minn:
                    minn = i - l + 1
                    minn_str = s[l:i + 1]

                # Remove the current leftmost character
                hashmap[s[l]] += 1
                l += 1
        return minn_str