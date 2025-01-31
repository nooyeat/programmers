import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
a = list(map(int, input().split()))
start = 0
end = n-1
count = 0
a.sort()

while end > start:
    if a[start] + a[end] == m:
        count+=1
        start+=1
    elif a[start] + a[end] > m:
        end-=1
    else:
        start+=1

print(count)