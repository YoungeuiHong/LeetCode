class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # 일단 정렬을 해야 함. start? end? 뭘 기준으로 정렬해야 할까.
        # 먼저 start 기준으로 정렬한 다음, end를 기준으로 정렬해야겠다.
        intervals.sort(key=lambda x: (x[0], x[1]))

        answer = []
        before = None

        for i in range(len(intervals)):
            interval = intervals[i]

            if before == None:
                before = interval
            else:
                if before[1] >= interval[0]:  # 합치는 조건: 이전 interval의 end가 현재 interval의 start보다 큰 경우
                    before = [before[0], max(before[1], interval[1])]
                else:  # 합칠 필요가 없다면 answer에 추가
                    answer.append(before)
                    before = interval

            if i == len(intervals) - 1 and before != None:
                answer.append(before)

        return answer


if __name__ == "__main__":
    s = Solution()
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    s.merge(intervals)

