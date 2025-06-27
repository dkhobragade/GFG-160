arr = [2, 4, 1, 3, 5]


first, second, third = float("-inf"), float("-inf"), float("-inf")


for i in arr:
    if i == first or i == second or i == third:
        continue
    if i > first:
        third = second
        second = first
        first = i
    elif i > second:
        third = second
        second = i
    elif i > third:
        third = i

    if third == float("-inf"):
        print(first)
print(third)
