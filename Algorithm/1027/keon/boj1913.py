n = int(input())
k = int(input())
snail = [[0 for i in range(n)] for _ in range(n)]
mr = [1, 0, -1, 0]
mc = [0, 1, 0, -1]
num = n**2
head = 0
r, c = 0, 0
ans = [-1, -1]
while snail[r][c] == 0:
    snail[r][c] = num
    if num == k:
        ans = [r + 1, c + 1]
    nr = r + mr[head]
    nc = c + mc[head]
    if nr < 0 or nc < 0 or nr > n - 1 or nc > n - 1:
        head = (head + 1) % 4
        nr = r + mr[head]
        nc = c + mc[head]
    if snail[nr][nc] != 0:
        head = (head + 1) % 4
        r = r + mr[head]
        c = c + mc[head]
    else:
        r = nr
        c = nc
    num -= 1
for i in range(n):
    print(*snail[i])
print(*ans)
