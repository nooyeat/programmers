def solution(N, stages):
    fail=[]
    stages.sort()
    cnt=[stages.count(i) for i in range(1,N+1)]
    len_stage=len(stages)
    for j in range(1,N+1):
        if cnt[j-1]!=0:
            fail.append(cnt[j-1]/len_stage)
            len_stage=len_stage-cnt[j-1]
        else:
            fail.append(0)
    a={i+1:j for i,j in enumerate(fail)}
    a=sorted(a.items(), key=lambda item:item[1], reverse=True)
    answer = [i[0] for i in a]
    return answer