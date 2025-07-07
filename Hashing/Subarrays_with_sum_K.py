arr = [10, 2, -2, -20, 10]
k = -10


count = 0
for i in range(len(arr)):
    sum = 0
    for j in range(i, len(arr)):
        sum += arr[j]
        if sum == k:
            count += 1
print(count)
