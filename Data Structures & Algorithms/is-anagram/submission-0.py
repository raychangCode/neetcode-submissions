class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        word_table = [0] * 26

        for i in range(len(s)):
            word_table[ord(s[i])-ord('a')] += 1
            word_table[ord(t[i])-ord('a')] -= 1

        for val in word_table:
            if val != 0:
                return False
        return True