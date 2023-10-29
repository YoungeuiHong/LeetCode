class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums or target not in nums:
            return [-1, -1]

        answer = []
        left = 0
        right = len(nums) - 1

        # 가장 처음 target이 되는 지점 찾기
        # 가장 처음 TRUE가 되는 지점 찾기
        # End를 리턴하기
        while left < right:
            mid = (left + right) // 2

            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        answer.append(right)

        # 가장 마지막으로 target이 되는 지점 찾기
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right + 1) // 2

            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid

        answer.append(left)

        return answer


if __name__ == "__main__":
    s = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    s.searchRange(nums, 8)
