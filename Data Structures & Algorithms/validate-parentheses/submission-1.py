class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            match c:
                case '(':
                    stack.append(0);
                case ')':
                    if len(stack) == 0 or stack.pop() != 0:
                        return False
                case '{':
                    stack.append(1);
                case '}':
                    if len(stack) == 0 or stack.pop() != 1:
                        return False
                case '[':
                    stack.append(2);
                case ']':
                    if len(stack) == 0 or stack.pop() != 2:
                        return False
        if len(stack):
            return False
        
        return True
            