def solution(X, Y):
    xy_set=set(X)&set(Y)

    if len(xy_set)==0:
        return '-1'
    
    elif len(xy_set)==1 and '0' in xy_set:
        return '0'
    
    new=[i*min(X.count(i), Y.count(i)) for i in xy_set]

    return ''.join(sorted(new, reverse=True))