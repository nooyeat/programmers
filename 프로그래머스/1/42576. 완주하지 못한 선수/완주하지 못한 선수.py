def solution(participant, completion):
    part = {}
    for i in participant:
        part[i] = part.get(i, 0) + 1
    for i in completion:
        part[i] -= 1
    return [key for key, val in part.items() if val > 0][0]