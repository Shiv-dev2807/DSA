class Solution:
    def isPalindrome(self, x: int) -> bool:
        li=[]
        for ch in str(x):
            li.append(ch)
        
        l = 0
        r = len(li)-1

        while l < r:
            if li[l] == li[r]:
                l+=1
                r-=1
            else:
                return False
        
        return True