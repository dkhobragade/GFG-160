arr = [12, 0]

# n = len(arr)

# prefix = [1] * n
# sufix = [1] * n

# res = [0] * n

# for i in range(1, n):
#     prefix[i] = arr[i - 1] * prefix[i - 1]

# print(prefix)

# for i in range(n - 2, -1, -1):
#     sufix[i] = arr[i + 1] * sufix[i + 1]

# print(sufix)

# for i in range(n):
#     res[i] = prefix[i] * sufix[i]

# print(res)


zeros = 0
idx = -1
prod = 1


for i in range(len(arr)):
    if arr[i] == 0:
        zeros += 1
        idx = i
    else:
        prod *= arr[i]

res = [0] * len(arr)

if zeros == 0:
    for i in range(len(arr)):
        res[i] = prod // arr[i]

elif zeros == 1:
    res[idx] = prod

print(res)
