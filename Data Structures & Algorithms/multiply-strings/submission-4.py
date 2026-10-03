class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return "0"

        n = len(num1)
        m = len(num2)
        ans = [0] * (n + m) # maximum length of possible answer

        for i in range(n - 1 , -1, -1):
            for j in range(m - 1, -1, -1):
                curr_prod = int(num1[i]) * int(num2[j])

                ans[i + j + 1] += curr_prod
                ans[i + j] += ans[i + j + 1] // 10 # carry
                ans[i + j + 1] %= 10

        idx = 0
        while idx < len(ans) and ans[idx] == 0:
            idx += 1

        return "".join(map(str, ans[idx:]))