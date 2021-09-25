from collections import deque


class Solution(object):
    def swimInWater(self, grid):

        visited = [[False] * len(grid) for i in range(len(grid))]

        path = self.bfs(grid, visited, 0, 0)

        return max(path)

    def bfs(self, grid, visited, row, col):

        path = []
        queue = deque()

        queue.append((row, col))

        visited[row][col] = True

        while (len(queue) > 0):
            cellTuple = queue.pop()
            r = cellTuple[0]
            c = cellTuple[1]
            path.append(grid[r][c])

            min_r = r
            min_c = c
            min_neighbour = 999999999
            min_r = r
            min_c = c

        # check left neighbour

        if c != 0:
            if not visited[r][c - 1]:
                visited[r][c - 1] = True
                if min(min_neighbour, grid[r][c - 1]) == grid[r][c - 1]:
                    min_r = r
                    min_c = c - 1
                    min_neighbour = grid[min_r][min_c]

        # check up neighbour

        if r != 0:
            if not visited[r - 1][c]:
                visited[r - 1][c] = True
                if min(min_neighbour, grid[r - 1][c]) == grid[r - 1][c]:
                    min_r = r - 1
                    min_c = c
                    min_neighbour = grid[min_r][min_c]

        # check right neighbour
        if c != len(grid) - 1:
            if not visited[r][c + 1]:
                visited[r][c + 1] = True
                if min(min_neighbour, grid[r][c + 1]) == grid[r][c + 1]:
                    min_r = r
                    min_c = c + 1
                    min_neighbour = grid[min_r][min_c]

        # check down neighbour
        if r != len(grid) - 1:
            if not visited[r + 1][c]:
                visited[r + 1][c] = True
                if min(min_neighbour, grid[r + 1][c]) == grid[r + 1][c]:
                    min_r = r + 1
                    min_c = c
                    min_neighbour = grid[min_r][min_c]

        if min_neighbour == 999999999:
            break

        queue.append((min_r, min_c))

    return path

    """
    :type grid: List[List[int]]
    :rtype: int
    """
