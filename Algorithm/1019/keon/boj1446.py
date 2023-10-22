import sys
read = sys.stdin.readline

n, d = map(int, read().split())
shortcut = []
dp = [int(i) for i in range(d + 1)]
for _ in range(n):
    u, v, dist = map(int, read().split())
    if v > d or v - u < dist:
        continue
    shortcut.append([u, v, dist])
shortcut.sort()

for i in range(d + 1):
    dp[i] = min(dp[i], dp[i - 1] + 1)
    while shortcut and shortcut[0][0] == i:
        u, v, dist = shortcut[0]
        del shortcut[0]
        dp[v] = min(dp[v], dp[i] + dist)
print(dp[d])
