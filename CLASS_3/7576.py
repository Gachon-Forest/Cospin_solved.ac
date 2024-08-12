from collections import deque

m,n=map(int,input().split())
box=[]
cannot=0
already=0
for i in range(n):
    row=list(map(int,input().split()))
    box.append(row)
    for j in row:
        if j==1:
            target=(i,j)
        if j==0:
            already+=1

moves=[(1,0),(0,1),(-1,0),(0,-1)]

queue=deque([target])

while queue:
    cnt=0
    x,y=queue.popleft()

    for dx,dy in moves:
        nx,ny=x+dx,y+dy

        if not 0<=nx<n or not 0<=ny<m or box[nx][ny]==-1:
            cnt+=1
        if cnt==4:
            cannot+=1
        if 0<=nx<n and 0<=ny<m and box[nx][ny]==0:
            box[nx][ny]=box[x][y]+1
            queue.append((nx,ny))

if already==0:
    print(0)
elif cannot==1:
    print(-1)
else:
    maximum=box[0][0]
    for row in box:
        for a in row:
            if maximum<a:
                maximum=a
    print(maximum-1)