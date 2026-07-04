class Solution:
    def reverseWords(self, s: str) -> str:
        listSt = list(s.split(" "))
        for i in range(len(listSt)):
            listSt[i] = list(listSt[i])
        

        for i in range(len(listSt)):
            start = 0
            last = len(listSt[i])-1
            while start < last:
                listSt[i][start], listSt[i][last] = listSt[i][last], listSt[i][start]
                start+=1
                last-=1
        
        nlist = []
        for i in range(len(listSt)-1):
            nlist.append((listSt[i]))
            nlist.append(" ")
        
        nlist.append((listSt[-1]))

        for i in range(len(nlist)):
            nlist[i] = "".join(nlist[i])
        
        return ("".join(nlist))