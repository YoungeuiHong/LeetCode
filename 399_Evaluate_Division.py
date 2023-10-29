from collections import defaultdict


class Solution:
    def calcEquation(self, equations, values, queries):
        graph = self.buildGraph(equations, values)
        results = [self.calculatePathWeight(start, end, set(), graph) for start, end in queries]
        return results

    # equations과 values를 바탕으로 그래프 생성
    def buildGraph(self, equations, values):
        # 딕셔너리의 딕셔너리 형태로 그래프 생성
        graph = defaultdict(dict)
        # a / b = 2라면 a-> 2 -> b 그리고 b -> 1/2 -> a
        for (u, v), weight in zip(equations, values):
            graph[u][v] = weight
            graph[v][u] = 1 / weight
        return graph

    # DFS 방식으로 start에서 end까지 가는 경로의 가중치 계산
    def calculatePathWeight(self, start, end, visited, graph):
        if start not in graph:
            return -1.0

        if end in graph[start]:
            return graph[start][end]

        visited.add(start)

        for neighbor, weight in graph[start].items():
            if neighbor not in visited:
                cumulativeWeight = self.calculatePathWeight(neighbor, end, visited, graph)
                if cumulativeWeight != -1.0:
                    return weight * cumulativeWeight

        return -1.0
