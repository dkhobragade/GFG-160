arr = ["act", "god", "cat", "dog", "tac"]

mp = {}
res = []

mp["dik"] = len(res)
print(res)

for i in range(len(arr)):
    s = arr[i]
    s = "".join(sorted(s))

    if s not in mp:
        mp[s] = len(res)
        res.append([])

    res[mp[s]].append(arr[i])

print(res)
