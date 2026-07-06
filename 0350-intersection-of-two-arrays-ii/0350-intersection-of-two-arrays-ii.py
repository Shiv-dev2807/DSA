class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l1 = sorted(nums1)
        l2 = sorted(nums2)
        p1 = 0
        p2 = 0
        l = []
        while p1 < len(l1) and p2 < len(l2):
            if l1[p1] == l2[p2]:
                l.append(l1[p1])
                p1+=1
                p2+=1
            elif l1[p1] > l2[p2]:
                p2+=1
            else:
                p1+=1
            
        
        return(l)