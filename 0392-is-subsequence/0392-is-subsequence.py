class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Walk through the longer string with a pointer for each string. When characters match, advance both pointers. Otherwise only advance the longer string's pointer.
        """
        if len(s) == 0:
            return True

        pA = 0
        pB = 0

        c = 0
        while pB < len(t):
            if s[pA] == t[pB]:
                pA+=1
                pB+=1
                c+=1
            else:
                pB+=1
            if c == len(s):
                return True
        
        return False