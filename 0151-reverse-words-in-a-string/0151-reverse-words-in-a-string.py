class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        newl = []
        i = len(l)-1

        while i >= 0:
            newl.append(l[i])
            i-=1
        
        news = " ".join(newl)
        return news