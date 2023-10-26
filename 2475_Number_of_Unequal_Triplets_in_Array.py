from itertools import combinations


class Solution(object):
    def unequalTriplets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = set(nums)
        if (len(nums_set) < 3):
            return 0

        result = 0
        for i in combinations(nums, 3):
            if i[0] == i[1] or i[1] == i[2] or i[0] == i[2]:
                continue
            result += 1

        return result
