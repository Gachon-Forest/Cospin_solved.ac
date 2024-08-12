n=int(input())
meetings=[]
start=0
cnt=0
for _ in range(n):
    meetings.append(list(map(int,input().split())))

meetings.sort(key=lambda x:(x[1],x[0]))

for i in range(n):
    if meetings[i][0]>=start:
        cnt+=1
        start=meetings[i][1]

print(cnt)