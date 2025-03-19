def solution(arr):
    a=min(arr)
    answer = []
    arr.remove(a)
    answer=arr
    if len(arr)==0:
        answer.append(-1)
    return answer