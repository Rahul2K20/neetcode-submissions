class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums) + 1
        count = [0] * n
        hmap = {}

        for i in nums:
            if i not in hmap:
                hmap[i] = 1
            else:
                hmap[i] += 1 

        for key,v in hmap.items():
            if count[v] == 0:
                count[v] = [key]
            else:
                count[v].append(key)

        res = []
        for i in range(len(nums), -1, -1):
            if count[i] != 0:
              res.extend(count[i])
            if len(res) == k:
                break

        return res 
        