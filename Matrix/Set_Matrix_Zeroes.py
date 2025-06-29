mat = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]

# n = len(mat)
# m = len(mat[0])

# rows = [False] * n
# cols = [False] * m


# for i in range(n):
#     for j in range(m):
#         if mat[i][j] == 0:
#             rows[i] = True
#             cols[j] = True


# for i in range(n):
#     for j in range(m):
#         if rows[i] or cols[j]:
#             mat[i][j] = 0

# print(mat)


col0 = 1
n = len(mat)
m = len(mat[0])

for i in range(n):
    for j in range(m):

        if mat[i][j] == 0:
            mat[i][0] = 0

            if j == 0:
                col0 = 0
            else:
                mat[0][j] = 0

for i in range(1, n):
    for j in range(1, m):
        if mat[i][0] == 0 or mat[0][j] == 0:
            mat[i][j] = 0

if mat[0][0] == 0:
    for j in range(m):
        mat[0][j] = 0

if col0 == 0:
    for i in range(n):
        mat[i][0] = 0

print(mat)
