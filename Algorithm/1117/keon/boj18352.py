import sys
import heapq
read = sys.stdin.readline


def dijkstra():
    ans = []
    n, m, k, x = map(int, read().split())
    graph = [[] for _ in range(n)]
    dist = [1000001 for _ in range(n)]
    for _ in range(m):
        a, b = map(int, read().split())
        graph[a - 1].append(b - 1)
    heap = []
    heapq.heappush(heap, [0, x - 1])
    dist[x - 1] = 0
    while heap:
        cost, cur = heapq.heappop(heap)
        if dist[cur] < cost:
            continue
        for nxt in graph[cur]:
            if dist[nxt] > cost + 1:
                dist[nxt] = cost + 1
                heapq.heappush(heap, [cost + 1, nxt])
    for i in range(n):
        if dist[i] == k:
            ans.append(i + 1)
    if ans:
        print(*ans, sep="\n")
    else:
        print(-1)


dijkstra()
