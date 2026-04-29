class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0
        for token in tokens:
            if token != '+' and token != '-' and token != '*' and token != '/':
                stack.append(int(token))
            else:
                if token == '+':
                    result = stack.pop() + stack.pop()
                elif token == '-':
                    temp = stack.pop()
                    result = stack.pop() - temp
                elif token == '*':
                    result = stack.pop() * stack.pop()
                else:
                    temp = stack.pop()
                    result = int(stack.pop() / temp)
                stack.append(result)
            print(result, stack)
        return stack[0]