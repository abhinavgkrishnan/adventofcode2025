from input import rolls
import numpy as np

matrix = np.array([[1 if char == '@' else 0 for char in line] 
                   for line in rolls.strip().split('\n')])

# print(len(matrix[0]))

count = 0
directions = [(-1, -1), (-1, 0), (-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1)]
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
                count += 1
            
print(count)