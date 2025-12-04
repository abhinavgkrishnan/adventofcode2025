from input import rolls
import numpy as np

matrix = np.array([[1 if char == '@' else 0 for char in line] 
                   for line in rolls.strip().split('\n')])
# print(len(matrix[0]))

def findValidRolls (matrix):
    directions = [(-1, -1), (-1, 0), (-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1)]
    removable = []
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            # print(matrix[i][j])
            if matrix[i][j] == 1:
                neighbor_count = 0
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols:
                        if matrix[ni][nj] == 1:
                            neighbor_count += 1
                if neighbor_count < 4:
                    removable.append((i,j))
    for i,j in removable:
        matrix[i][j] = 0
    return len(removable);

total = 0 
while True:
    count = findValidRolls(matrix)
    total += count
    if count == 0:
        break
print(total)