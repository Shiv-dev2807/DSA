class Solution:
    def isHappy(self, n: int) -> bool:
        if n <= 0:
            return False

        seen = set()

        while n != 1:
            if n in seen:
                return False

            seen.add(n)

            l = list(map(int, str(n)))

            s = 0
            for i in range(len(l)):
                s += l[i] ** 2

            n = s

        return True