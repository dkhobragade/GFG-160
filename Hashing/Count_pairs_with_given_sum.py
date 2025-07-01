arr = [1, 1, 1, 1]
target = 2

count = 0

for i in range(1, len(arr) - 1):
    for j in range(len(arr) - 1):
        if arr[i] + arr[j] == target:
            count += 1


print(count)
