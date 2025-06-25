mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

n = len(mat)  # row
m = len(mat[0])  # column

res = []

while m != 0:
    for i in range(n):
        res.append(mat[i][m - 1])
    m -= 1
print(res)
