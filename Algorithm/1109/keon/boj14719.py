import sys
read = sys.stdin.readline

h, w = map(int, read().split())
blocks = [*map(int, read().split())]
dp = [-1 for _ in range(w)]
dp[0] = blocks[0]
ans = 0
for i in range(1, w):
    dp[i] = max(blocks[i], dp[i - 1])
minn = blocks[-1]
for i in range(w - 1, -1, -1):
    minn = max(minn, blocks[i])
    dp[i] = min(minn, dp[i])
    if dp[i] > blocks[i]:
        ans += (dp[i] - blocks[i])
print(ans)
