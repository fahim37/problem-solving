class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        temp = sorted(nums)
        ret = {}
        for i,v in enumerate(temp):
            if v not in ret:
                ret[v] = i
        res = []
        for v in nums:
            res.append(ret[v])
        return res

                