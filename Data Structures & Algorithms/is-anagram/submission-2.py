class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hmap_s = {}
        for i in s:
            if i not in hmap_s:
                hmap_s[i] = 1
            else:
                hmap_s[i] += 1 

        for j in t: 
            if j in hmap_s:
                hmap_s[j] -= 1 
                if hmap_s[j] < 0: 
                    return False 
            else:
                return False 
        
        return True 