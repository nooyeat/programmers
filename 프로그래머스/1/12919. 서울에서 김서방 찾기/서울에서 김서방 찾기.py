def solution(seoul):
    answer=-1
    for i in seoul:
        answer += 1
        if i =="Kim":
            j="김서방은 {}에 있다".format(answer)
    return j
   