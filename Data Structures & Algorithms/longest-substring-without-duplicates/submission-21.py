class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        r = 0
        window  = 0
        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]]+1, l)
            mp[s[r]] = r
            window = max(window, r - l + 1)
        return window