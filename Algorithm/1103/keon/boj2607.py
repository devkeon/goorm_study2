n = int(input())
words = [input() for _ in range(n)]
ans = 0

for s in words[1:n]:
    word = list(words[0])
    flag = 0
    for c in s:
        if c in word:
            word.remove(c)
        else:
            if flag == 1:
                break
            else:
                flag = 1
    else:
        if len(word) <= 1:
            ans += 1
print(ans)
