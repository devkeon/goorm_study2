# BOJ 1446
import sys
read = sys.stdin.readline

n, d = map(int, read().split())
shortcuts = [list(map(int, read().split())) for _ in range(n)]
dp = [i for i in range(d+1)] # 0부터 d까지의 수


for i in range(len(dp)):
    for start, end, shortcut_dist in shortcuts:
        if i == start and end <= d:
            dp[end] = min(dp[end], dp[start] + shortcut_dist)

    if i+1 <= d:
        dp[i+1] = min(dp[i+1], dp[i] + 1)

print(dp[d])


""" 
0부터 d까지의 수를 순환하면서 
shortcuts를 돌며 요소(시작점, 끝점, 지름 길이)를 꺼내 쓴다.

만약 i가 지금 지름길의 시작점과 같고 끝점이 총 길이 이내에 있다면
end 까지의 길이가 두 경우 중 더 작은  값을 dp[end]에 저장


dp[end] : 지름길을 사용하지 않고 끝점까지 가는 이동거리
dp[start] + shortcut_dist : 지름길을 사용하여 끝점까지 가는 이동거리


배열의 범위가 넘어가지 않는 선에서 
바로 다음 지점을 갈 때 
지름길을 사용한 경우(dp[i+1])와 그냥 직진한 경우(dp[i]+1)중 
더 적은 값을 바로 다음 지점까지 가는 최솟값으로 지정
""" 