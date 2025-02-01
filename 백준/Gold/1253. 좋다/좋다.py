import sys
input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
cnt = 0
num.sort()

for i in range(len(num)):
    start = 0
    end = n-1
    while end > start:
        if num[start] + num[end] == num[i]:
            if start != i and end != i:
                cnt+=1
                break
            
            elif start == i:
                start+=1
                
            elif end == i:
                end-=1
            
        elif num[start] + num[end] > num[i]:
            end-=1
            
        else:
            start+=1
print(cnt)