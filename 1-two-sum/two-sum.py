class Solution(object):
    def twoSum(self, nums, target):
        hash_map = {}
        for i,v in enumerate(nums):
            diff = target-v
            if diff in hash_map:
                return [i,hash_map[diff]]
            else:
                hash_map[v] = i
        