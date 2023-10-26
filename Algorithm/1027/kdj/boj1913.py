n = int(input())
m = int(input())
xm, ym = 0, 0

snail = [[0 for i in range(1, n+1)] for _ in range(1, n+1)]
xc, yc = n // 2, n // 2
num = 1
snail[xc][yc] = num
num += 1

directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] 

steps = 1
i = 0
while num <= n * n:
    for _ in range(2):
        d = directions[i % 4]
        for _ in range(steps):
            if num > n * n: 
                break
            xc += d[0]
            yc += d[1]
            
            if(num == m):
                xm, ym = xc+1, yc+1

            snail[xc][yc] = num
            num += 1
        i += 1
    steps += 1

for i in snail:
    print(*i)

print(xm, ym)
