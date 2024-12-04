def solution(s):
    answer = []
    
    j=0
    for i in s:
        if i not in s[:j]:
            answer.append(-1)
            j+=1
        else:
            answer.append(j-s[:j].rfind(i))
            j+=1
    return answer