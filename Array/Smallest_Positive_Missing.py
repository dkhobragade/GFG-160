arr = [2, -3, 4, 1, 1, 7]

# arr.sort()

# res = 1

# for i in range(len(arr)):
#     if res == arr[i]:
#         res += 1

#     elif res < arr[i]:
#         break
# print(res)


n = len(arr)

for i in range(n):

    while 1 <= arr[i] <= n and arr[i] != arr[arr[i] - 1]:

        temp = arr[i]
        arr[i] = arr[arr[i] - 1]
        arr[temp - 1] = temp

print(arr)

for i in range(1, n + 1):
    if i != arr[i - 1]:
        print(i)
        break
