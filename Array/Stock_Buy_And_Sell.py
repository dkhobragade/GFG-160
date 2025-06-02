prices = [100, 180, 260, 310, 40, 535, 695]
# prices = [4, 2, 2, 2, 4]

# Method 1

# profit = 0

# for i in range(1, len(prices)):
#     if prices[i] > prices[i - 1]:
#         profit += prices[i] - prices[i - 1]

# print(profit)


# Method 2

lMin = prices[0]
lMiax = prices[0]

profit = 0
i = 0

while i < len(prices) - 1:

    while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
        i += 1
    lmin = prices[i]

    while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
        i += 1
    lmax = prices[i]

    profit += lmax - lmin

print(profit)
