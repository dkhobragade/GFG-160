stalls = [1, 2, 4, 8, 9]
k = 3


def check(stalls, k, dist):
    cnt = 1
    prev = stalls[0]

    for i in range(1, len(stalls)):
        if stalls[i] - prev >= dist:
            prev = stalls[i]
            cnt += 1

    return cnt >= k


stalls.sort()
res = 0

low = 1
high = stalls[-1] - stalls[0]

while low <= high:
    mid = low + (high - low) // 2

    if check(stalls, k, mid):
        res = mid
        low = mid + 1
    else:
        high = mid - 1

print(res)
