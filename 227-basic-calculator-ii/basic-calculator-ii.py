class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        op = '+'
        s = s.replace(" ", "")  # remove spaces for easier processing

        for i, ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)  # build multi-digit numbers

            if not ch.isdigit() or i == len(s) - 1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                elif op == '/':
                    prev = stack.pop()
                    # truncate toward zero
                    stack.append(int(prev / num))

                op = ch
                num = 0

        return sum(stack)
