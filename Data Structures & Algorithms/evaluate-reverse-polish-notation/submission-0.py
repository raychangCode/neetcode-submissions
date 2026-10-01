class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t not in '+-*/':
                stack.append(int(t))
            
            else:
                sec = stack.pop()
                fir = stack.pop()

                if t == "+":
                    stack.append(fir + sec)
                if t == "-":
                    stack.append(fir - sec)
                if t == "*":
                    stack.append(fir * sec)
                if t == "/":
                    stack.append(int(fir / sec))

        return stack[-1]