class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxWindow = 0
        maxP = 0
        myset = set()
        for r in range(len(s)):
            while s[r] in myset:
                myset.remove(s[l])
                l += 1
            if s[r] not in myset:
                myset.add(s[r])
            maxWindow = (r - l + 1)
            maxP=max(maxWindow,maxP)
        return maxP
        

            

        