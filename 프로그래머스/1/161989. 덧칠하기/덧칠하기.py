def solution(n, m, section):
    answer = 0
    count=1
    standard=section[0]
    for i in section:
        if standard+m-1<i:
            count+=1
            standard=i
    answer=count
    return answer