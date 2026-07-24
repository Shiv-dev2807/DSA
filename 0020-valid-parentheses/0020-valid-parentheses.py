class Solution:
    def isValid(self, s: str) -> bool:
        op = ['(','[','{']

        stack = []

        index = 0

        while index < len(s):
            if s[index] in op:
                stack.append(s[index])
            else:
                if not stack:
                    return False
                else:
                    a = stack.pop()
                    if s[index] == ')' and a != '(' or s[index] == ']' and a != '[' or s[index] == '}' and a != '{':
                        return False
            index+=1
        
        return len(stack) == 0