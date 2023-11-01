import sys
import copy
read = sys.stdin.readline

n, k = map(int, read().split())
tube = [list(map(int, read().split())) for _ in range(n)]
s, x, y = map(int, read().split())

test_tube = copy.deepcopy(tube)
dx=[0,0,-1,1]
dy=[-1,1,0,0]

for _ in range(s):
  num = 1
  while num <= k:
    for tx in range(len(tube)):
      for ty in range(len(tube[tx])):
        if tube[tx][ty] == num:
          for i in range(4):
            nx = tx + dx[i]
            ny = ty + dy[i]
            if nx>=0 and nx<n and ny>=0 and ny<n:
              if test_tube[nx][ny] == 0:
                test_tube[nx][ny] = tube[tx][ty]
    tube = copy.deepcopy(test_tube)
    num += 1

print(tube[x-1][y-1])
