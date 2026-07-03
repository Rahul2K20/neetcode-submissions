class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0 

        for i in seen:
            if i-1 not in seen:
                length = 1
                next_num = i+1 
                while next_num in seen:
                    length += 1 
                    next_num += 1 
                longest = max(length, longest)

        return longest 
            
