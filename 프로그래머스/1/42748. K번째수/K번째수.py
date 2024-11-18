def solution(array, commands):
    answer = []
    for i in commands:
        a=i[0]-1
        b=i[1]
        c=i[2]-1
        answer.append(sorted(array[a:b])[c])
    return answer