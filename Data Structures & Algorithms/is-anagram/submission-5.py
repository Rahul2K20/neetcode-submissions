class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 

        hmap_s = {}

        for c in s: 
            if c in hmap_s:
                hmap_s[c] += 1
            else:
                hmap_s[c] = 1
        
        for c in t:
            if c in hmap_s:
                hmap_s[c] -=1
                if hmap_s[c] < 0:
                    return False 
            else:
                return False 
        return True 
