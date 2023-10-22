import sys
import heapq
read = sys.stdin.readline

n, k = map(int, read().split())
lab = [[*map(int, read().split())] for _ in range(n)]
# heap 요소 = [현재 초, 현재 바이러스, 행, 열]
heap = []
mr, mc = [0, 1, 0, -1], [1, 0, -1, 0]

for i in range(n):
    for j in range(n):
        if lab[i][j] != 0:
            heapq.heappush(heap, [0, lab[i][j], i, j])
s, x, y = map(int, read().split())

while heap and heap[0][0] < s:
    sec, v, cr, cc = heapq.heappop(heap)
    for i in range(4):
        nr, nc = cr + mr[i], cc + mc[i]
        # 바이러스는 번호가 작은게 먼저 점령한다 했으므로 동시성 문제 x
        if 0 <= nr < n and 0 <= nc < n and lab[nr][nc] == 0:
            lab[nr][nc] = v
            heapq.heappush(heap, [sec + 1, v, nr, nc])
print(lab[x - 1][y - 1])
