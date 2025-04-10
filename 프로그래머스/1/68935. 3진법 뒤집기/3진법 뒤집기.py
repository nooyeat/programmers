def solution(n):
    answer=0
    s=[]
    while n>=1:
        s.append(n%3)
        n=n//3
    for i in range(len(s)):
        answer += ((3**(len(s)-i-1))*s[i])
        
    return answer