class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter1 = Counter(s1)
        counter2 = Counter()
        n = len(s1)

        def valid(d1, d2):
            for k in d1:
                if k not in d2 or d1[k] > d2[k]:
                    return
            return True

        for i in range(len(s2)):
            counter2[s2[i]] += 1

            # window size > n
            if i >= n:
                counter2[s2[i - n]] -= 1

                if counter2[s2[i - n]] == 0:
                    del counter2[s2[i - n]]

            # window size == n
            if i >= n - 1:
                if valid(counter1, counter2):
                    return True

        return False