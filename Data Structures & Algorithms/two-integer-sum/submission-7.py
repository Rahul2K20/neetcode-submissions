class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(0,len(nums)):
            # i + j = target
            # j = target - i 
            j = target - nums[i]
            if j in hmap:
                return [hmap[j], i]

            hmap[nums[i]] = i
