class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        for word in words:
            i = 0
            j = len(word)-1
            isPal = True
            while i < j:
                if word[i] == word[j]:
                    i +=1
                    j-=1
                    isPal = True
                else:
                    isPal = False
                    break
            
            if isPal:
                return word
        
        return ""