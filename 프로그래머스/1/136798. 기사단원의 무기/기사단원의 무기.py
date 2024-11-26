import math
def solution(number, limit, power):
    answer = 0
    measure=[]
    for i in range(1, number+1):
        sum=0
        for mea in range(1,int(i**(1/2)+1)):
            if i%mea==0:
                sum+=1
                if mea**2 != i:
                    sum+=1
        measure.append(sum)
    for j in measure:
        if j > limit:
            answer+=power
        else:
            answer+=j
    return answer