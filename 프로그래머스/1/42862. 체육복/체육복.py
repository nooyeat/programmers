def solution(n, lost, reserve):
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)
    
    for i in sorted(lost_set):
        if i - 1 in reserve_set:
            reserve_set.remove(i-1)
            lost_set.remove(i)
        elif i + 1 in reserve_set:
            reserve_set.remove(i+1)
            lost_set.remove(i)
    return n - len(lost_set)