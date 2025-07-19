arr = [1, 2, 0, 3]


n = len(arr)
total_sum = sum(arr)
left_sum = 0


for i in range(n):
    total_sum -= arr[i]

    if total_sum == left_sum:
        print(i)
        break
    left_sum += arr[i]
