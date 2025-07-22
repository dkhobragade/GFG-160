arr = [10, 3, 5, 6, 2]

n = len(arr)

prefix = [1] * n
sufix = [1] * n

res = [0] * n

for i in range(1, n):
    prefix[i] = arr[i - 1] * prefix[i - 1]

print(prefix)

for i in range(n - 2, -1, -1):
    sufix[i] = arr[i + 1] * sufix[i + 1]

print(sufix)

for i in range(n):
    res[i] = prefix[i] * sufix[i]

print(res)
