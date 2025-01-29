import sys
input = sys.stdin.readline
n, m = map(int, input().split())
numlist = [[0]*(n+1)]
sumlist = [[0]*(n+1) for x in range(n+1)]

for i in range(n):
    row = [0] + [int(i) for i in input().split()]
    numlist.append(row)

for i in range(1, n+1):
    for j in range(1, n+1):
        sumlist[i][j] = sumlist[i][j-1] + sumlist[i-1][j] - sumlist[i-1][j-1] + numlist[i][j]

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(sumlist[x2][y2] - sumlist[x1-1][y2] - sumlist[x2][y1-1] + sumlist[x1-1][y1-1])