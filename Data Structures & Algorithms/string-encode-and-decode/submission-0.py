class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = []

        for word in strs:
            ans.append(str(len(word)))
            ans.append('#')
            ans.append(word)

        return "".join(ans)

    def decode(self, s: str) -> List[str]:
        ans = []
        left = 0

        while left < len(s):
            right = left

            while s[right] != '#':
                right += 1

            length = int(s[left:right])
            word_start = right + 1
            word_end = word_start + length
            ans.append(s[word_start: word_end])
            left = word_end

        return ans