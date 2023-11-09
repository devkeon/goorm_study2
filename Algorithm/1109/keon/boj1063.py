import sys
read = sys.stdin.readline

coldex = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
move = {"R": 0, "L": 1, "B": 2, "T": 3, "RT": 4, "LT": 5, "RB": 6, "LB": 7}
mr = [0, 0, 1, -1, -1, -1, 1, 1]
mc = [1, -1, 0, 0, 1, -1, 1, -1]
k, s, n = read().split()
king = [8 - int(k[1]), coldex[k[0]]]
stone = [8 - int(s[1]), coldex[s[0]]]

for _ in range(int(n)):
    d = move[read().rstrip()]
    nr = king[0] + mr[d]
    nc = king[1] + mc[d]
    nrr = nr + mr[d]
    ncc = nc + mc[d]
    if 0 <= nr < 8 and 0 <= nc < 8:
        if stone == [nr, nc] and 0 <= nrr < 8 and 0 <= ncc < 8:
            king = [nr, nc]
            stone = [nrr, ncc]
        elif stone != [nr, nc]:
            king = [nr, nc]
print(list(coldex.keys())[king[1]] + str(8 - king[0]))
print(list(coldex.keys())[stone[1]] + str(8 - stone[0]))
