import sys

read = sys.stdin.readline
n = int(read())
dp = [0 for _ in range(n)]
stairs = [int(read()) for _ in range(n)]
dp[0] = stairs[0]
if 2 <= n:
    dp[1] = stairs[0] + stairs[1]
if 3 <= n:
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

for i in range(3, n):
    dp[i] = max(dp[i - 2], dp[i - 3] + stairs[i - 1]) + stairs[i]
print(dp[n - 1])
