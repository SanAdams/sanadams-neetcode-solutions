class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'[': ']', '(': ')', '{': '}'}
        
        for char in s:
            if char in pairs:  # If it's an opening character
                stack.append(char)
            elif char in pairs.values():  # If it's a closing character
                if not stack or pairs[stack.pop()] != char:
                    return False
        
        return not stack
