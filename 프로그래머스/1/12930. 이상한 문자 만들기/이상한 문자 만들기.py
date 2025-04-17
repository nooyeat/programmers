def solution(s):
    answer = ''
    new=s.split(' ')
    result=[]
    for i in new:
        word=''
        for idx,j in enumerate(i):
            if idx%2==0:
                word+=j.upper()
            else:
                word+=j.lower()
        result.append(word)
    return " ".join(result)
