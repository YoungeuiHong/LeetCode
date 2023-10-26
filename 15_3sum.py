class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for left in range(len(nums) - 2):
            if left > 0 and nums[left] == nums[left - 1]:  # 중복 방지
                continue
            mid = left + 1
            right = len(nums) - 1
            while mid < right:
                curr_sum = nums[left] + nums[mid] + nums[right]
                if curr_sum < 0:
                    mid += 1
                elif curr_sum > 0:
                    right -= 1
                else:
                    result.append([nums[left], nums[mid], nums[right]])
                    while mid < right and nums[mid] == nums[mid + 1]:
                        mid += 1
                    while mid < right and nums[right] == nums[right - 1]:
                        right -= 1
                    mid += 1
                    right -= 1

        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    solution.threeSum(nums)
