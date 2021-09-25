grid1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

grid2 = [
    ["0", "0", "0"],
    ["0", "1", "1"],
    ["0", "0", "0"]
]


def numIslands(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print("\n\nfor i,j {},{}".format(i, j))
            dfs_value = dfs(grid, i, j)
            print("dfs value for i,j {},{}, grid {} : {}".format(
                i, j, grid[i][j], dfs_value))
            count += dfs_value

    # print(grid)
    return count


def dfs(grid, i, j):
    print("dfs called for i,j {},{}".format(i, j))
    if i < 0 or i > len(grid)-1 or j < 0 or j > len(grid[i])-1 or grid[i][j] == '0':
        print("returning 0 for i,j {},{}".format(i, j))
        return 0

    print("setting i,j to 0: {},{}; prev value: {}".format(i, j, grid[i][j]))
    grid[i][j] = '0'

    dfs(grid, i+1, j)
    dfs(grid, i-1, j)
    dfs(grid, i, j+1)
    dfs(grid, i, j-1)
    print("returning 1 for i {}, j {}".format(i, j))
    return 1


if __name__ == '__main__':
    print(numIslands(grid2))
