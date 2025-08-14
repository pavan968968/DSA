class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # Each element: [char, count]

        for ch in s:
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([ch, 1])

        # Build result
        return "".join(char * count for char, count in stack)
