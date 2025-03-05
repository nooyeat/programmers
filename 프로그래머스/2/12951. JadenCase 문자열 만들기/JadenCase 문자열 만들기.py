def solution(s):
    answer = s[0].upper()
    s = s.lower()
    for i in range(1, len(s)):
        if s[i-1] == ' ' and s[i] != ' ':
            answer += s[i].upper()
        else:
            answer += s[i]
    return answer