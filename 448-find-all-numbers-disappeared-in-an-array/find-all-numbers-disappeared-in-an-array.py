class Solution(object):
    def findDisappearedNumbers(self, nums):
        unique = set(nums)
        ret = []
        for i in range(1,len(nums)+1):
            if i not in unique:
                ret.append(i)

        return ret
        