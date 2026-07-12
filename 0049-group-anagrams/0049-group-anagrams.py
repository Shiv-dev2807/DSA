class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            h[sorted_word].append(word)        
        
        return list(h.values())