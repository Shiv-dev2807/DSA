class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stacka = []
        stackb = []
        i = 0
        j = 0
        while i < len(s) :
            if s[i] != '#':
                stacka.append(s[i])
            elif len(stacka) != 0 and s[i] == '#':
                stacka.pop()
            i+=1

        while j < len(t):
            if t[j] != '#':
                stackb.append(t[j])
            elif len(stackb) != 0 and t[j] == '#':
                stackb.pop()
            
            j+=1

        return stacka == stackb