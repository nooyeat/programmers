def solution(k, score):
    answer=[]
    new=[]
    for i in range(len(score)):
        if i<=k-1:
            new.append(score[i])
            answer.append(min(new))
        else:
            if min(new)<score[i]:
                new.append(score[i])
                new.remove(min(new))
                answer.append(min(new))
            else:
                answer.append(min(new))
    return answer