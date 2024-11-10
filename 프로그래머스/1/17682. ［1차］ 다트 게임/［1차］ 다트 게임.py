import re
def solution(dartResult):
    answer = 0
    scores=[]
    segments = re.findall(r'(\d+)([SDT])([*#]?)', dartResult)
    for i in segments:
        score, bonus, prise = i
        score=int(score)
        if bonus == 'D':
            score **=2
        elif bonus == 'T':
            score **=3
        
        if prise == '*':
            if scores:
                scores[-1]*=2
            score*=2
        elif prise == '#':
            score *=-1
        scores.append(score)
    answer=sum(scores)
    return answer