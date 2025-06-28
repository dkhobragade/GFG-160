mat = [[87, 96, 99], [101, 103, 111]]
x = 101


n = len(mat)
m = len(mat[0])

# i = 0
# j = m - 1


# while i < n and j >= 0:
#     if mat[i][j] == x:
#         print(True)
#         break
#     elif mat[i][j] < x:
#         i += 1
#     else:
#         j -= 1

low = 0
high = n * m - 1

while low <= high:
    mid = low + (high - low) // 2

    row = mid // m
    col = mid % m

    if mat[row][col] == x:
        print(True)
        break
    elif mat[row][col] > x:
        high = mid - 1
    else:
        low = mid + 1
