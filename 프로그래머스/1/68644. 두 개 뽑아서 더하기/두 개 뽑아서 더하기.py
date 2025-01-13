def solution(numbers):
    answer = []
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            new = numbers[i] + numbers[j]
            answer.append(new)

    return sorted(list(set(answer)))