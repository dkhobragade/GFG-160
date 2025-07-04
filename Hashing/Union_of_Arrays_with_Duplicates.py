a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]


set = set()

for i in range(len(a)):
    set.add(a[i])


for i in range(len(b)):
    set.add(b[i])

res = []
for i in set:
    res.append(i)
print(res)
