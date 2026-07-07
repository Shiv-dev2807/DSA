class Solution:
    def sumAndMultiply(self, n: int) -> int:
        l = list(str(n))
        summ = 0
        xl = []
        for n in l:
            if int(n) !=0:
                xl.append((n))
                summ = summ+int(n)
        if xl:
            x = int("".join(xl))

            return(x*summ)
        else:
            return 0