def solution(players, callings):
    player = {j:i for i, j in enumerate(players)}
    rank = {i:j for i, j in enumerate(players)}
    
    for i in callings:
        cur_rank = player[i]
        pre_rank = cur_rank - 1
        pre_player = rank[pre_rank]
        
        player[i], player[pre_player] = pre_rank, cur_rank
        rank[cur_rank], rank[pre_rank] = pre_player, i
        
    return [i for i in rank.values()]