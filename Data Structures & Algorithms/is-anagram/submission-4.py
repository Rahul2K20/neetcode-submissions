class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 

        hmap = {}
        for i in s:
            if i not in hmap:
                hmap[i] = 1 
            else:
                hmap[i] += 1 

        for i in t: 
            if i in hmap:
                hmap[i] -= 1 
                if hmap[i] < 0:
                    return False 
            else:
                return False 

        return True 
        