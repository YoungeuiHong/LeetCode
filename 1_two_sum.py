class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        answer = [];

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    answer = [i, j]

        return answer

if __name__ == '__main__':
    solution = Solution()
    nums = [2,7,11,15]
    target = 9
    result = solution.twoSum(nums, target)
    print(result)
