class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for word in strs:
            count_table = [0] * 26

            for char in word:
                count_table[ord(char) - ord('a')] += 1

            ans[tuple(count_table)].append(word)

        return list(ans.values())