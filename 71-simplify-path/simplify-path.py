class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split("/")

        for part in parts:
            if part == "" or part == ".":
                # skip empty or current directory
                continue
            elif part == "..":
                # go one directory up if possible
                if stack:
                    stack.pop()
            else:
                # push valid directory name
                stack.append(part)

        # join stack into final path
        return "/" + "/".join(stack)
