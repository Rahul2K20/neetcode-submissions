class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap = {}
        for i in range (len(nums)):
            if nums[i] not in hmap:
                hmap[nums[i]] = i 
            else: 
                return True 
        return False 
         