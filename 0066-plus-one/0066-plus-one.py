class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(map(str, digits)))
        n = str(num+1)
        l=[]
        for i in n:
            l.append(int(i))
        return(l)