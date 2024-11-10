def solution(lottos, win_nums):
    answer = []
    cnt=0
    cnt2=3
    cnt3=3
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            cnt+=1
            
    if 0 in lottos:
        if cnt>=2:
            for j in range(2,7):
                if cnt == j:
                    answer.append(j+cnt2)
                cnt2-=2
        else:
            answer.append(6)

        cnt+=lottos.count(0)

        for j in range(2,7):
            
            if cnt == j:
                answer.append(j+cnt3)
            cnt3-=2
    else:
        if cnt>2:
            for j in range(2,7):
                    if cnt == j:
                        answer.append(j+cnt2)
                        answer.append(j+cnt2)
                    cnt2-=2
        else:
            answer.append(6)
            answer.append(6)
                
    return sorted(answer)