import sys
read = sys.stdin.readline


def solution():
    n, m = map(int, read().split())
    graph = [list(map(int, read().split())) for _ in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    for _ in range(m):
        u, v, c = map(int, read().split())
        if graph[u - 1][v - 1] <= c:
            print("Enjoy other party")
        else:
            print("Stay here")


solution()
