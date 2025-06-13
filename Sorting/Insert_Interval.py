intervals = [[1, 3], [4, 5], [6, 7], [8, 10]]
newInterval = [5, 6]


# intervals.append(newInterval)

# intervals.sort()

# print(intervals)

# res = [intervals[0]]
# print(res[-1])

# for i in range(1, len(intervals)):
#     last = res[-1]
#     cur = intervals[i]

#     if cur[0] <= last[1]:
#         last[1] = max(last[1], cur[1])
#     else:
#         res.append(cur)
# print(res)


res = []
i = 0
n = len(intervals)

while i < n and intervals[i][1] < newInterval[0]:
    res.append(intervals[i])
    i += 1

while i < n and intervals[i][0] <= newInterval[1]:
    newInterval[0] = min(intervals[i][0], newInterval[0])
    newInterval[1] = max(intervals[i][1], newInterval[1])
    i += 1

res.append(newInterval)

while i < n:
    res.append(intervals[i])
    i += 1

print(res)
