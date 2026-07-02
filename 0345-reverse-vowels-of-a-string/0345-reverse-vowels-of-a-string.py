class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        st = ['a','e','i','o','u','A','E','I','O','U']

        l = 0
        r = len(s)-1

        while l<=r:
            if s[l] in st and s[r] in st:
                s[l],s[r] = s[r],s[l]
                l+=1
                r-=1
            elif s[l] not in st:
                l+=1
            else:
                r-=1
        
        return "".join(s)
