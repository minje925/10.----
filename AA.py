n = int(input())
alist = list(map(int, input().split()))
result = [0]*len(alist)
for i, a in enumerate(alist):
    cnt = 0
    for j in range(len(result)):
        if cnt == a and result[j] == 0:
            result[j] = i+1
            break
        if result[j] == 0:
            cnt+=1

for r in result:
    print(r, end=' ')
