class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        st = ""
        last = len(s)-1
        chl = []
        for ch in s:
            chl.append(ch)
        
        while last >=0:
            if chl[last] == " ":
                chl[last] = ""
                last-=1
            else:
                last = len(s)-1
                break
        
        while last >=0:
            if chl[last] != " ":
                st += chl[last]
                last-=1
            else:
                break
        
        return(len(st))