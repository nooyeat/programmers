import sys
input = sys.stdin.readline
n, m = map(int, input().split())
num = list(map(int, input().split()))
sum_list = [0] * n
c = [0] * m
cnt = 0
sum_list[0] = num[0]

for i in range(1, n):
    sum_list[i] = sum_list[i-1] + num[i]

for i in range(n):
    remain = sum_list[i] % m
    if remain == 0:
        cnt+=1
    c[remain] += 1

for i in range(m):
    if c[i]>1:
        cnt+=(c[i]*(c[i]-1)//2)

print(cnt)