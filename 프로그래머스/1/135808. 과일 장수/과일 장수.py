def solution(k, m, score):
    answer = 0
    box=[]
    score.sort(reverse=True)
    s=len(score)%m
    if s>0:
        score=score[:-s]
    for i in range(0, len(score), m):
        box=score[i:i+m]
        answer+=m*min(box)
    
    return answer