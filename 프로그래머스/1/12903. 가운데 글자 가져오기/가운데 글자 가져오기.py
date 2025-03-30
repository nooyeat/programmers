def solution(s):
    i=int(len(s)/2)
    if len(s)==1:
        answer=s[0]
    elif len(s)%2 ==0:   
        answer=s[i-1:i+1]
    else:
        answer=s[i]
    return answer