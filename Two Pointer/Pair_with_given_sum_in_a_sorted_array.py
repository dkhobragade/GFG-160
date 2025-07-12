arr = [-1, 1, 5, 5, 7]
target = 6

count = 0

for i in range(len(arr)):
    for j in range(i, len(arr)):
        if arr[i] + arr[j] == target:
            count += 1

print(count)
