class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = set(["+", "-", "*", "/"])

        for character in tokens:
            match character:
                case "+":
                    stack.append(stack.pop() + stack.pop())
                case "-":
                    b, a = stack.pop(), stack.pop()
                    stack.append(a - b)
                case "*":
                    stack.append(stack.pop() * stack.pop())
                case "/":
                    b, a = stack.pop(), stack.pop()
                    stack.append(int(a / b))
                case _:
                    stack.append(int(character))

        return stack[0]