def solution(answers):
    ans=[[1,2,3,4,5], [2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    correct=[0,0,0]
    for i in range(3):
        stud=ans[i]
        stud_ans=stud*(len(answers)//len(stud))+stud[:len(answers)%len(stud)]
        correct_score=0
        for j in range(len(answers)):
            if answers[j]==stud_ans[j]:
                correct_score+=1
        correct[i]=correct_score
    answer = [idx+1 for idx, score in enumerate(correct) if max(correct)==score]
    return answer