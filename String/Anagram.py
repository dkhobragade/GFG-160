s1 = "geeks"
s2 = "kseeg"

hashmap = {}

for i in s1:
    hashmap[i] = hashmap.get(i, 0) + 1


for i in s2:
    hashmap[i] = hashmap.get(i, 0) - 1

for i in hashmap.values():
    if i != 0:
        print("no")
        break

print(hashmap)
