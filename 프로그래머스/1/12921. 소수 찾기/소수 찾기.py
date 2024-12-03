def prime(num):
    if num==2:
        return True
    if num%2==0:
        return False
    for i in range(3, int(num**0.5)+1,2):
        if num%i==0:
            return False
    return True
def solution(n):
    answer = 0
    for j in range(2, n+1):
        if prime(j):
            answer+=1
    return answer