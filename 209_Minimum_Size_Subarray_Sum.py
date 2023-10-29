class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        def available_subarray(target, nums, size):
            for start in range(len(nums) - size + 1):
                if sum(nums[start:start + size]) >= target:
                    return True
            return False

        exist = False
        left = -1
        right = len(nums) + 1

        # 가장 처음 available_subarray가 True가 되는 지점을 찾아야 함
        while left + 1 < right:
            mid = (left + right) // 2

            if available_subarray(target, nums, mid):
                exist = True
                right = mid
            else:
                left = mid

        if exist:
            return right
        else:
            return 0
