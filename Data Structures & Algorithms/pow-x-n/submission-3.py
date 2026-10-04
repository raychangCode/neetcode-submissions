class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0 or x == 1:
            return x
        if n == 0:
            return 1

        ans = 1
        N = abs(n)
        while N > 0:
            if N % 2 == 1:
                ans *= x
                N -= 1

            else:
                x *= x
                N //= 2

        if n > 0:
            return ans
        return 1 / ans