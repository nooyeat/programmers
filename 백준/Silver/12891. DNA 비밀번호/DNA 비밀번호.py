s, p = map(int, input().split())
password = list(input())
min_list = list(map(int, input().split()))
min_dict = {'A':min_list[0], 'C':min_list[1], 'G':min_list[2], 'T':min_list[3]}
cnt = 0
my_pass = password[:p]
my_dict = {'A':0, 'C':0, 'G':0, 'T':0}

for i in my_pass:
    my_dict[i] += 1

def test():
    return all(my_dict[i]>=min_dict[i] for i in 'ACGT')

if test():
    cnt+=1

for i in range(s-p):
    new_out = password[i]
    new_in = password[i+p]
    my_dict[new_out]-=1
    my_dict[new_in]+=1
    if test():
        cnt+=1
    
print(cnt)