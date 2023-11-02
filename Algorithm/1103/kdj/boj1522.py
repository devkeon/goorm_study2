s = input()
n = len(s)
total_a = s.count('a')

extended_s = s + s

min_swaps = total_a
for i in range(n):
    current_swaps = total_a - extended_s[i:i+total_a].count('a')
    min_swaps = min(min_swaps, current_swaps)

print(min_swaps)


#aaabbaba aaabbaba
#aaaaabbb