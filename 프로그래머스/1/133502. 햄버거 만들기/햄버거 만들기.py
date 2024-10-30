def solution(ingredient):
    answer = 0
    list_ingredient=[]
    for i in ingredient:
        list_ingredient.append(i)
        if len(list_ingredient)>=4 and list_ingredient[-4:]==[1,2,3,1]:
            answer+=1
            del list_ingredient[-4:]
    return answer