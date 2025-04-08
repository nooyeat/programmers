def solution(n, m):
    answer = []
    for i in range(1,n+1):
        for j in range(1,m+1):
            if n/i==m/j and len(answer)==0:
                answer.append(int(n/i))
    if n>=m:
        for a in range(1,n+1):
            for b in range(1,n+1):
                if a*n==b*m and len(answer)==1:
                    answer.append(int(a*n))
    else:
        for a in range(1,m+1):
            for b in range(1,m+1):
                if a*n==b*m and len(answer)==1:
                    answer.append(int(a*n))
    return answer