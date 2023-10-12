# BOJ 2579 - 계단 오르기
# 1. 입력 받기(n만큼 받아 arr에 저장)
# 2. 0번째, 1번째 dp값은 각각 arr[0], arr[0] + arr[1]
# 3. dp - 2번째 부터 i번째 순서에서의 합(최대)은 [i번째 값] + [i-2까지의 최댓값] or [i번째 값] + [i-1번째 값] + [i-3번째까지의 최댓값] 중 더 큰 값
# 4. 2의 경우를 dp에 저장, 마지막 값 출력

n = int(input())
arr = [int(input()) for _ in range(n)]

dp = [0 for _ in range(n)]

dp[0] = arr[0]
if n > 1:
    dp[1] = arr[0] + arr[1]

for i in range(2, n):
    dp[i] = max(dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i])

print(dp[n-1])