arr = [0, -1, 2, -3, 1]

temp = []
n = len(arr)

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if arr[i] + arr[j] + arr[k] == 0:
                temp.append([i, j, k])
print(temp)
