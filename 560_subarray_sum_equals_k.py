class Solution(object):
    def subarraySum(self, nums, k):
        result = 0 # 가능한 경우의 수
        prefix_sum = 0 # 누적 합
        d = {0: 1} # 누적 합의 dictionary

        for i in nums:
            prefix_sum = prefix_sum + i

            # (현재까지의 누적합 prefix_sum - 목표값 k)가 누적 합 dictionary에 있다면
            # 목표값 k를 만들 수 있는 구간이 존재한다는 것
            # 가능하 경우의 수에 d[prefix_sum - k]만큼을 추가
            if prefix_sum - k in d:
                result = result + d[prefix_sum - k]

            # 딕셔너리의 값 채워 넣기
            if prefix_sum not in d:
                d[prefix_sum] = 1
            else:
                d[prefix_sum] = d[prefix_sum] + 1

        return result


if __name__ == '__main__':
    nums = [1, 2, 3]
    solution = Solution()
    result = solution.subarraySum(nums, 3)
    print(result)
