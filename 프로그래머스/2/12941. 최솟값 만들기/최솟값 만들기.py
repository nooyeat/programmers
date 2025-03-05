def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    return sum([i*j for i, j in zip(A, B)])