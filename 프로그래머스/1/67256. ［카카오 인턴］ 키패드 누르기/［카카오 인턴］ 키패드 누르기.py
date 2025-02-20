def solution(numbers, hand):
    answer = ''
    left, right = '*', '#'
    for i in numbers:
        if i in [1, 4, 7]:
            left = i
            answer+='L'
        elif i in [3, 6, 9]:
            right = i
            answer+='R'
        else:
            if left == i:
                answer+='L'
            elif right == i:
                answer+='R'
            else:
                l, r = 0, 0
                if i == 2:
                    length = {1:[1, 3, 5],
                              2:[4, 6, 8],
                              3:[7, 9, 0],
                              4:['*', '#']}
                elif i == 5:
                    length = {1:[2, 4, 6, 8],
                              2:[1, 3, 7, 9, 0],
                              3:['*', '#']}
                elif i == 8:
                    length = {1:[5, 7, 9, 0],
                              2:[2, 4, 6, '*', '#'],
                              3:[1, 3]}
                else:
                    length = {1:[8, '*', '#'],
                              2:[5, 7, 9],
                              3:[2, 4, 6],
                              4:[1, 3]}
                for j in length:
                    if left in length[j]:
                        l = j
                    if right in length[j]:
                        r = j

                if l == r:
                    if hand == 'left':
                        answer+='L'
                        left = i
                    else:
                        answer+='R'
                        right = i
                elif l > r:
                    answer+='R'
                    right = i
                else:
                    answer+='L'
                    left = i

    return answer