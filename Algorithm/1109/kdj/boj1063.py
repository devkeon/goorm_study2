# input_str = input().split()

# chessX = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# chessY = ['1', '2', '3', '4', '5', '6', '7', '8']
# move = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']

# king = list(input_str[0])
# stone = list(input_str[1])
# n = int(input_str[2])

# for i in range(n):
#   one_move = input()
#   if one_move == move[0]:
#     if king[0] == chessX[-1]:
#       continue
#     else:
#       king[0] = chessX[chessX.index(king[0])+1]
#       if king == stone:
#         if stone[0] == chessX[-1]:
#           king[0] = chessX[chessX.index(king[0])-1]
#         else:
#           stone[0] = chessX[chessX.index(stone[0])+1]
#   elif one_move == move[1]:
#     if king[0] == chessX[0]:
#       continue
#     else:
#       king[0] = chessX[chessX.index(king[0])-1]
#       if king == stone:
#         if stone[0] == chessX[0]:
#           king[0] = chessX[chessX.index(king[0])+1]
#         else:
#           stone[0] = chessX[chessX.index(stone[0])-1]
#   elif one_move == move[2]:
#     if king[1] == chessY[0]:
#       continue
#     else:
#       king[1] = chessY[chessY.index(king[1])-1]
#       if king == stone:
#         if stone[1] == chessY[-1]:
#           king[1] = chessY[chessY.index(king[1])+1]
#         else:
#           stone[1] = chessY[chessY.index(stone[1])-1]
#   elif one_move == move[3]:
#     if king[1] == chessY[-1]:
#       continue
#     else:
#       king[1] = chessY[chessY.index(king[1])+1]
#       if king == stone:
#         if stone[1] == chessY[0]:
#           king[1] = chessY[chessY.index(king[1])-1]
#         else:
#           stone[1] = chessY[chessY.index(stone[1])+1]
#   elif one_move == move[4]:
#     if king[0] == chessX[-1] or king[1] == chessY[-1]:
#       continue
#     else:
#       king[0] = chessX[chessX.index(king[0])+1]
#       king[1] = chessY[chessY.index(king[1])+1]
#       if king == stone:
#         if stone[0] == chessX[-1] or stone[1] == chessY[-1]:
#           king[0] = chessX[chessX.index(king[0])-1]
#           king[1] = chessY[chessY.index(king[1])-1]
#         else:
#           stone[0] = chessX[chessX.index(stone[0])+1]
#           stone[1] = chessY[chessY.index(stone[1])+1]
#   elif one_move == move[5]:
#     if king[0] == chessX[0] or king[1] == chessY[-1]:
#       continue
#     else:
#       king[0] = chessX[chessX.index(king[0])-1]
#       king[1] = chessY[chessY.index(king[1])+1]
#       if king == stone:
#         if stone[0] == chessX[0] or stone[1] == chessY[-1]:
#           king[0] = chessX[chessX.index(king[0])+1]
#           king[1] = chessY[chessY.index(king[1])-1]
#         else:
#           stone[0] = chessX[chessX.index(stone[0])-1]
#           stone[1] = chessY[chessY.index(stone[1])+1]
#   elif one_move == move[6]:
#     if king[0] == chessX[-1] or king[1] == chessY[0]:
#       continue
#     else:
#       king[0] = chessX[chessX.index(king[0])+1]
#       king[1] = chessY[chessY.index(king[1])-1]
#       if king == stone:
#         if stone[0] == chessX[-1] or stone[1] == chessY[0]:
#           king[0] = chessX[chessX.index(king[0])-1]
#           king[1] = chessY[chessY.index(king[1])+1]
#         else:
#           stone[0] = chessX[chessX.index(stone[0])+1]
#           stone[1] = chessY[chessY.index(stone[1])-1]
#   elif one_move == move[7]:
#     if king[0] == chessX[0] or king[1] == chessY[0]:
#       continue
#     else:
#       king[0] = chessX[chessX.index(king[0])-1]
#       king[1] = chessY[chessY.index(king[1])-1]
#       if king == stone:
#         if stone[0] == chessX[0] or stone[1] == chessY[0]:
#           king[0] = chessX[chessX.index(king[0])+1]
#           king[1] = chessY[chessY.index(king[1])+1]
#         else:
#           stone[0] = chessX[chessX.index(stone[0])-1]
#           stone[1] = chessY[chessY.index(stone[1])-1]

# print(''.join(king))
# print(''.join(stone))

input_str = input().split()
king = list(input_str[0])
stone = list(input_str[1])
n = int(input_str[2])

chessX = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
chessY = ['1', '2', '3', '4', '5', '6', '7', '8']
moves = {'R': (1, 0), 'L': (-1, 0), 'B': (0, -1), 'T': (0, 1), 'RT': (1, 1), 'LT': (-1, 1), 'RB': (1, -1), 'LB': (-1, -1)}

def get_new_position(position, dx, dy, chessX, chessY):
    x_index = chessX.index(position[0]) + dx
    y_index = chessY.index(position[1]) + dy
    if 0 <= x_index < len(chessX) and 0 <= y_index < len(chessY):
        return [chessX[x_index], chessY[y_index]]
    return position

def move_piece(piece, direction, chessX, chessY):
    dx, dy = moves[direction]
    return get_new_position(piece, dx, dy, chessX, chessY)

for _ in range(n):
    one_move = input()
    new_king = move_piece(king, one_move, chessX, chessY)
    
    if new_king == stone:
        new_stone = move_piece(stone, one_move, chessX, chessY)
        if new_stone != stone:
            king = new_king
            stone = new_stone
    else:
        king = new_king

print(''.join(king))
print(''.join(stone))
