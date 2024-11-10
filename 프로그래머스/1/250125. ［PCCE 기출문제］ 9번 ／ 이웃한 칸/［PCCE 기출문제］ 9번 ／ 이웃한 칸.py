def solution(board, h, w):
    answer = 0
    direct=[(0,1), (1,0), (-1,0), (0,-1)]
    for dh, dw in direct:
        nh=h+dh
        nw=w+dw
        if 0<= nh <len(board) and 0<=nw<len(board[0]):
            if board[h][w]==board[nh][nw]:
                answer+=1
    return answer