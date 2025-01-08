def solution(s):
    answer = True
    a=s.lower().count('p')
    b=s.lower().count('y')
    if a==b:
        answer= True
    elif a==0 and b==0:
        answer= True
    elif a!=b:
        answer =False

    return answer