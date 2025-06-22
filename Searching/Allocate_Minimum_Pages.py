arr = [12, 34, 67, 90]
k = 2


def check(arr, k, pagelimit):
    cnt = 1
    pagesum = 0

    for pages in arr:
        if pagesum + pages > pagelimit:
            cnt += 1
            pagesum = pages

        else:
            pagesum += pages

    return cnt <= k


low = max(arr)
high = sum(arr)
res = -1

while low <= high:
    mid = low + (high - low) // 2

    if check(arr, k, mid):
        res = mid
        high = mid - 1
    else:
        low = mid + 1

print(res)
