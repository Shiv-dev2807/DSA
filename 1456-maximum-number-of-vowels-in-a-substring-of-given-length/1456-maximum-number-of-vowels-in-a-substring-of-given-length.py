class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a','e','i','o','u']
        maxV = 0
        v = 0

        i = 0
        p = k-1
        while p<len(s):
            if i == 0:
                for j in range(i,p+1):
                    if s[j] in vowels:
                        v += 1
                i+=1
                p+=1
            else:
                
                
                if s[p] in vowels and s[i-1] not in vowels:
                    v = v + 1
                
                elif s[p] not in vowels and s[i-1] in vowels:
                    v = v-1

                
                i+=1
                p+=1
            if v > maxV:
                maxV = v
        
        return(maxV)