from collections import deque

def BFS(matrix, visited, row, col):
    queue = deque()

    # add the starting element to the queue
    queue.append((row, col))

    print(f"queue now {queue}")
    visited[row][col]=True

    while len(queue) > 0:
        cellTuple = queue.popleft()
        r = cellTuple[0]
        c = cellTuple[1]

        print(matrix[r][c])

        # go to all neighbours

        # left neighbour
        if c!= 0:
            # print(f"Trying left of r {r}, c {c}, visited for {r}{c-1} {visited[r][c-1]}")
            if not visited[r][c - 1]:
                queue.append((r, c - 1))
                visited[r][c-1] = True
                # print(f"queue left {queue}")

        # up neighbour
        if r != 0:
            # print(f"Trying up of r {r}, c {c}, visited for {r-1}{c} {visited[r-1][c]}")
            if not visited[r - 1][c]:
                queue.append((r - 1, c))
                visited[r-1][c] = True
                # print(f"queue up {queue}")

        # right neighbour
        if c != len(matrix[0])-1:
            # print(f"Trying right of r {r}, c {c}, visited for {r}{c+1} {visited[r][c+1]}")
            if not visited[r][c + 1]:
                queue.append((r, c + 1))
                visited[r][c + 1] = True
                # print(f"queue right {queue}")

        # down neighbour
        if r != len(matrix)-1:
            # print(f"Trying down of r {r}, c {c}, visited for {r+1}{c} {visited[r+1][c]}")
            if not visited[r + 1][c]:
                queue.append((r + 1, c))
                visited[r + 1][c] = True
                # print(f"queue down {queue}")


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

visited = [[False] * len(matrix[0]) for i in range(len(matrix))]

BFS(matrix, visited, 0, 0)
