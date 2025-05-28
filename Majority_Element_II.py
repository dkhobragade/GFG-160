import math

arr = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]

# Normal

# temp = []

# for i in arr:
#     if arr.count(i) >= math.ceil(len(arr) / 3) and i not in temp:
#         temp.append(i)

# print(sorted(temp))

# hashMap

# count = {}
# temp2 = []

# for i in arr:
#     count[i] = count.get(i, 0) + 1
# print(count)

# for key, val in count.items():

#     if val > len(arr) / 3:
#         temp2.append(key)

# print(temp2)

# if len(temp) == 2 and temp2[0] > temp2[1]:
#     temp2[0], temp2[1] = temp2[0], temp2[1]

# print(temp2)


# Moore Voting

n = len(arr)
res = []

ele1, ele2 = -1, -1
count1, count2 = 0, 0

for i in arr:
    if i == ele1:
        count1 += 1
    elif i == ele2:
        count2 += 1
    elif count1 == 0:
        ele1 = i
        count1 += 1
    elif count2 == 0:
        ele2 = i
        count2 += 1
    else:
        count1 -= 1
        count2 -= 1

cnt1, cnt2 = 0, 0

for i in arr:
    if ele1 == i:
        cnt1 += 1
    elif ele2 == i:
        cnt2 += 1

if cnt1 > n / 3:
    res.append(ele1)
if cnt2 > n / 3 and ele1 != ele2:
    res.append(ele2)

if len(res) == 2 and res[0] > res[1]:
    res[0], res[1] = res[1], res[0]

print(res)
