n = int(input())
score = list(map(int, input().split()))
score_max = max(score)
print(sum(score)/score_max*100/n)