def solution(a, b):
    answer = ''
    day=[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week=['FRI','SAT','SUN','MON','TUE','WED','THU']
    c=0
    if a==1:
        c=b%7
        answer=week[c-1]
    else:
        for i in range(a-1):
            c+=day[i]
        c+=b
        c%=7
        answer=week[c-1]
    return answer