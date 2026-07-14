class Solution:
    def isValid(self, s: str) -> bool:
        hashs = {")":"(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c in hashs:
                if stack and stack[-1] == hashs[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
        

        