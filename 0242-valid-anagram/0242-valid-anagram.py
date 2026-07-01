class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hs = {}
        ht = {}

        for i in range(len(s)):
            hs[s[i]] = hs.get(s[i],0)+1
        
        for j in range(len(t)):
            ht[t[j]] = ht.get(t[j],0)+1
        
        return hs == ht