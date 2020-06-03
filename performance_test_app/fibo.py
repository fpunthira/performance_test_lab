matrix = [[1, 0, 0, 1, 0], [1, 0, 1, 0, 0], [0, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 0]]
a = []
def riverSizes(matrix):
    # Write your code here.
    for y in range(0,len(matrix)):
        count = 0
        for x in range(0,len(matrix[y])):
            if matrix[x+1][y] == 1 or matrix[x-1][y] == 1 or matrix[x][y+1] == 1 or matrix[x][y-1] == 1 and matrix[x,y]:
                print(str(x)+","+str(y))

    pass


print(riverSizes(matrix))