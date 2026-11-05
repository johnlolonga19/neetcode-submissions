class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        unique = set()
        ans = 0

        while r < len(s):
            if s[r] not in unique:
                ans = max(ans, r - l + 1)
                unique.add(s[r])
                r += 1
            else:
                while s[r] in unique:
                    unique.remove(s[l])
                    l += 1
        return ans
                



        