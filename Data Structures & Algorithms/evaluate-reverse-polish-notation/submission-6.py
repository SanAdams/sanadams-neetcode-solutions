class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            
            elif char == "/":
                a = int (stack.pop())
                b = int (stack.pop())
                stack.append(int(float(b) / a))

            elif char == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            
            elif char == "-":
                a = int (stack.pop())
                b = int (stack.pop())
                stack.append(b-a)
            else:
                stack.append(int(char))
        return stack[0]
