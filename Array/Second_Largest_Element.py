arr = [12, 35, 1, 10, 34, 1]


temp1 = -1
temp2 = -1

for i in arr:
    if i > temp1:
        temp2 = temp1
        temp1 = i
    elif i > temp2 and temp2 != temp1:
        temp2 = i

print("Second Largest Element ", temp2)
