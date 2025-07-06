from collections import defaultdict

arr = ["act", "god", "cat", "dog", "tac"]

# mp = {}
# res = []

# for i in range(len(arr)):
#     s = arr[i]
#     s = "".join(sorted(s))

#     if s not in mp:
#         mp[s] = len(res)
#         res.append([])

#     res[mp[s]].append(arr[i])

# print(res)


ans = defaultdict(list)

for s in arr:
    count = [0] * 26
    for c in s:
        count[ord(c) - ord("a")] += 1
    ans[tuple(count)].append(s)

print(list(ans.values()))
