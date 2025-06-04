s = "geeksforgeeks"

hashmap = {}

for i in s:
    hashmap[i] = hashmap.get(i, 0) + 1

for key, value in hashmap.items():
    if value == 1:
        print(key)
        break

# print(hashmap)
