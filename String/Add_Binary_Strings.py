s1 = "00100"
s2 = "010"

n = max(len(s1), len(s2))
carry = 0
result = ""

s1 = s1.zfill(n)
s2 = s2.zfill(n)

for i in range(n - 1, -1, -1):
    a = int(s1[i])
    b = int(s2[i])

    total = a + b + carry

    if total == 0:
        result = "0" + result
        carry = 0
    elif total == 1:
        result = "1" + result
        carry = 0
    elif total == 2:
        result = "0" + result
        carry = 1
    else:
        result = "1" + result
        carry = 1

if carry:
    result = "1" + result


def removeLeadingZero(s):
    first = s.find("1")
    return s[first:] if first != -1 else "0"


print(removeLeadingZero(result))
