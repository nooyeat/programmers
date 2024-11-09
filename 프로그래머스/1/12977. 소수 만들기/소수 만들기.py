def prime(num):
    if num>1:
        for i in range(2, num):
            if num%i==0:
                return False
    return True

def solution(nums):
    answer = 0
    for x in range(len(nums)):
        for y in range(x+1, len(nums)):
            for z in range(y+1, len(nums)):
                sum=nums[x] + nums[y] +nums[z]
                if prime(sum)==True:
                    answer+=1
    return answer