mat = [[87, 96, 99], [101, 103, 111]]
x = 105


n = len(mat)
m = len(mat[0])

i = 0
j = m - 1


while i < n and j >= 0:
    if mat[i][j] == x:
        print(True)
        break
    elif mat[i][j] < x:
        i += 1
    else:
        j -= 1
