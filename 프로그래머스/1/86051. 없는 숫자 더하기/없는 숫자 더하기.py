def solution(numbers):
    a=[0,1,2,3,4,5,6,7,8,9]
    answer=0
    for i in a:
        if i not in numbers:
            answer=answer+i
    return answer