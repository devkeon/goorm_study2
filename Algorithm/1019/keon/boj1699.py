import math
n = int(input())

ans, square = 0, []
limit = math.floor(math.sqrt(n))
dp = [float('inf') for _ in range(n + 1)]

for i in range(1, limit + 1):
    dp[i**2] = 1
    square.append(i**2)
for i in square:
    for j in range(i, n + 1):
        dp[j] = min(dp[j], dp[j - i] + 1)
print(dp[n])
