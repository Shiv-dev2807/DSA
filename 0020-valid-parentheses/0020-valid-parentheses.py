class Solution:
    def isValid(self, s: str) -> bool:
        op = ['(','[','{']

        stack = []
        i = 0
        
        while i < len(s):
            if s[i] in op:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                else:
                    a = stack.pop()
                    if (s[i] == ')' and a != '(') or (s[i] == ']' and a != '[') or (s[i] == '}' and a != '{'):
                        return False
            
            i+=1
        
        return len(stack) == 0