# TODO

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def find_parent(parents, a):
            if parents[a] != a:
                parents[a] = find_parent(parents, parents[a])
            return parents[a]

        def union_parent(parents, a, b):
            a_parent = find_parent(parents, a)
            b_parent = find_parent(parents, b)

            if a_parent < b_parent:
                parents[b_parent] = a_parent
            else:
                parents[a_parent] = b_parent

        row = len(grid)
        col = len(grid[0])
        parents = [0] * (row * col)

        # 부모 테이블 초기화
        for i in range(row * col):
            parents[i] = i

        for i in range(row):
            for j in range(col):

if __name__ == "__main__":
    s = Solution()
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    s.numIslands(grid)
