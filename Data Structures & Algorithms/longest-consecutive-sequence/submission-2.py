class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        #O (nlogn)
        ans = sorted(nums)

        count = 1 
        longest = 1
        for i in range (len(ans)-1):
            if (ans[i+1] == ans[i]):
                continue 
            if (ans[i+1] - ans[i]) == 1:
                count += 1 
            else: 
                count = 1 
            longest = max(count, longest)

        return longest