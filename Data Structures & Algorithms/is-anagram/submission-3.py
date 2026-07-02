class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        
        else: 
            hmap_s={}
            #create word count of every word in s
            for i in s:
                if i not in hmap_s:
                    hmap_s[i] = 1 
                else:
                    hmap_s[i] += 1 

            #loop through t and check if it exists in s
            for i in t:
                if i in hmap_s: 
                    hmap_s[i] -= 1
                    if hmap_s[i] < 0: 
                        return False 
                else:
                    return False 
            return True 
                