mat = [[3, 30, 38], [20, 52, 54], [35, 60, 69]]
x = 62


# for i in range(len(mat)):
#     for j in range(len(mat[0])):
#         if mat[i][j] == x:
#             print(True)
#             break

n = len(mat)
m = len(mat[0])

i = 0
j = m - 1

while i < n and j >= 0:
    if mat[i][j] > x:
        j -= 1
    elif mat[i][j] < x:
        i += 1
    else:
        print(True)
        break
print(False)
