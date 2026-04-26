class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ')' : '(', '}' : '{', ']' : '[' }

        for c in s:
            # 1) closing bracket
            if c in closeToOpen:
                # a) if stack is not empty and last elem is the "open" of same type parenthesis
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                # b) if stack is empty or the last elem is not of the same type
                else:
                    return False
            # 2) opening bracket
            else:
                stack.append(c)
        
        return True if not stack else False # check if stack is empty at the end