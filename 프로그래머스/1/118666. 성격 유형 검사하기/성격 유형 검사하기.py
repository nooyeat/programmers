def solution(survey, choices):
    answer = ''
    score = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'A':0, 'N':0, 'M':0}
    transed_score = {1:3, 2:2, 3:1, 5:1, 6:2, 7:3}
    choices_idx = 0
    
    for i in survey:
        if choices[choices_idx] >= 5:
            score[i[1]] += transed_score[choices[choices_idx]]
        elif choices[choices_idx] == 4:
            score[i[0]] += 0
            score[i[1]] += 0
        else:
            score[i[0]] += transed_score[choices[choices_idx]]
        choices_idx+=1
        
    if score['R'] >= score['T']:
        answer += 'R'
    else:
        answer += 'T'
    if score['C'] >= score['F']:
        answer += 'C'
    else:
        answer += 'F'
    if score['J'] >= score['M']:
        answer += 'J'
    else:
        answer += 'M'
    if score['A'] >= score['N']:
        answer += 'A'
    else:
        answer += 'N'    
    print(score)

    return answer