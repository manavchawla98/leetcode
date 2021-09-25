def matrixDiagonal(mat):
    #diagonals of elements in top most row
    for i, elem in enumerate(mat[0]):
        print(f"element is {elem}")


mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
matrixDiagonal(mat)


