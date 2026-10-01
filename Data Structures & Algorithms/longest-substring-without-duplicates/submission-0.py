class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        ans = 0
        n = len(s)
        seen = set()

        while right < n:

            if s[right] not in seen:
                ans = max(ans, right - left + 1)
                seen.add(s[right])
                right += 1
            else:
                while left <= right and s[right] in seen:
                    seen.remove(s[left])
                    left += 1

        return ans