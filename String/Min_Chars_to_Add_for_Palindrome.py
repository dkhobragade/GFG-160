s = "abc"


# def isPalindrome(s, i, j):
#     while i < j:
#         if s[i] != s[j]:
#             return False
#         i += 1
#         j -= 1
#     return True


# def minChar(s):
#     cnt = 0
#     i = len(s) - 1

#     while i >= 0 and not isPalindrome(s, 0, i):
#         i -= 1
#         cnt += 1

#     return cnt


# print(minChar(s))


def computeLpsArray(pat):

    n = len(pat)
    lps = [0] * n

    len_lps = 0

    i = 1

    while i < n:

        if pat[i] == pat[len_lps]:
            len_lps += 1
            lps[i] = len_lps
            i += 1

        else:

            if len_lps != 0:
                len_lps = lps[len_lps - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def minChar(s):
    n = len(s)
    rev = s[::-1]

    s = s + "$" + rev

    lps = computeLpsArray(s)

    return n - lps[-1]


print(minChar(s))
