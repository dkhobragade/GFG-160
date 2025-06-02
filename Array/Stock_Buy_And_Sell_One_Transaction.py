# prices = [7, 10, 1, 3, 6, 9, 2]
# prices = [1, 3, 6, 9, 11]
prices = [61, 44, 70, 78, 73, 95, 27, 1]


# Method 1

# profit = 0

# for i in range(len(prices) - 1):
#     for j in range(i + 1, len(prices) - 1):
#         dif = prices[j] - prices[i]
#         if profit < dif:
#             profit = dif

# print(profit)


# Method 2

min_price = prices[0]
profit = 0

for i in prices[1:]:
    if i < min_price:
        min_price = i
    else:
        diff = i - min_price
        profit = max(profit, diff)

print(profit)
