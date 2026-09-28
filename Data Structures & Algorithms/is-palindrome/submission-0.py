class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        def alphaNum(char):
            return (ord('A') <= ord(char) <= ord('Z') or 
            (ord('a') <= ord(char) <= ord('z')) or
            (ord('0') <= ord(char) <= ord('9')))

        while left < right:
            while left < right and not alphaNum(s[left]):
                left += 1
            while left < right and not alphaNum(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True