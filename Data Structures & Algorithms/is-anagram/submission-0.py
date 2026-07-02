class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hmaps = {}
        for i in s:
            if i not in hmaps:
                hmaps[i] = 1
            else:
                hmaps[i] += 1
        
        for i in t:
            if i in hmaps:
                hmaps[i] -= 1
                if hmaps[i] < 0:
                    return False 

            else : 
                return False 


        return True
