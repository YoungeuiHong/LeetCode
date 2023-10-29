from collections import deque


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        # 모든 과목에 대한 진입 차수는 0으로 초기화
        indegree = [0] * numCourses

        # 각 과목에 연결된 간선 정보를 담기 위한 그래프 초기화
        graph = [[] for _ in range(numCourses)]

        # 선수 과목 관계를 그래프에 반영하기
        for edge in prerequisites:
            u, v = edge  # 수업 u를 듣기 위해선 v를 먼저 들어야 함
            graph[v].append(u)  # v -> u

            indegree[u] += 1  # u의 진입 차수 1 증가

        result = []  # 수강할 수 있는 과목 목록
        q = deque()

        # 진입 차수가 0인 과목들을 큐에 삽입
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        # 큐가 빌 때까지 반복
        while q:
            now = q.popleft()
            result.append(now)

            for i in graph[now]:
                # now 과목과 연결된 노드들의 진입 차수에서 1 빼기
                indegree[i] -= 1
                # 새롭게 진입 차수가 0이 되는 과목들을 큐에 삽입
                if indegree[i] == 0:
                    q.append(i)

        # 들을 수 있는 과목 수가 numCourses보다 적으면 False 리턴
        return len(result) == numCourses
