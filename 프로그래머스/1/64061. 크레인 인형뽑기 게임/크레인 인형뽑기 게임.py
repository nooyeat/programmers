def solution(board, moves):
    answer = 0
    crain_result = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0 :
                crain_result.append(board[j][i-1])
                board[j][i-1] = 0
                break
    i = 0
    while i<len(crain_result)-1:
        if crain_result[i] == crain_result[i+1]:
            del crain_result[i:i+2]
            answer +=2
            i=0
        else:
            i+=1
    return answer