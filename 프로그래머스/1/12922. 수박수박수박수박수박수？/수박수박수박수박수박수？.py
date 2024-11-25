def solution(n):
    if n%2==0:
        for i in range(n):
            answer='수박'*int(n/2)
    else:
        for i in range(n):
            answer='수박'*int(n/2)+'수'
    return answer