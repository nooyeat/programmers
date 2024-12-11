def solution(phone_number):
    answer = list(phone_number)
    for i in range(len(phone_number)-4):
        answer[i] = '*'
    answer = ''.join(answer)
    return answer