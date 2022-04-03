def gen_board(n):
    return [[0]*n for x in range(n)]

def print_board(board):
    boardsize = len(board)
    numlen = len(str(boardsize**2))
    print(boardsize * ('+' + numlen * '-') + '+')
    for line in board:
        for sqr in line:
            print(f'|{sqr:{numlen}}', end='')
        print('|\n' + boardsize * ('+' + numlen * '-') + '+')

def poss_moves(x, y, board, predict=True):
    boardsize = len(board)
    moves = [(x-1, y+2), (x+1, y+2), (x+2, y+1), (x+2, y-1),
             (x-1, y-2), (x+1, y-2), (x-2, y+1), (x-2, y-1)]
    moves = [m for m in moves if 0 <= m[0] < boardsize and 0 <= m[1] < boardsize
                                 and board[m[1]][m[0]] == 0]
    if not predict:
        return moves
    else: # optimize using Warnsdorff's rule
        movesdict = {m:len(poss_moves(m[0], m[1], board, False)) for m in moves}
        sortmoves = [x[0] for x in sorted(movesdict.items(), key=lambda x:x[1])]
        return sortmoves

def gen_tour(x, y, movecount, board, closed=False):
    board[y][x] = movecount
    if movecount == len(board) ** 2:
        return board
    else:
        for move in poss_moves(x, y, board):
            return gen_tour(move[0], move[1], movecount+1, board)
        board[y][x] = 0

def main():
    board = gen_board(8)
    x = gen_tour(0, 0, 1, board)
    print_board(x)

if __name__ == '__main__':
    main()
