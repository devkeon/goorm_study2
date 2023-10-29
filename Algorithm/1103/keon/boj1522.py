seq = input()
acount, bcount = 0, 0
for k in seq:
    if k == 'a':
        acount += 1
    else:
        bcount += 1
ans = float('inf')
n = len(seq)
for i in range(n):
    cnt = 0
    for j in range(i, i + bcount):
        ind = j
        if j >= n:
            ind -= n
        if seq[ind] == 'a':
            cnt += 1
    ans = min(cnt, ans)
print(ans)
