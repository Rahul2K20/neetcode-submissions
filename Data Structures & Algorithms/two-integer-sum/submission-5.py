class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range (len(nums)):
            x = target - nums[i]
            if x not in hmap:
                hmap[nums[i]] = i
            else:    
             return [hmap[x], i]
            
        