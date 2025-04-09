def solution(d, budget):
    answer=0
    a=sorted(d)
    for i in a:
        if budget>=i:
            budget =budget-i
            answer+=1
    return answer