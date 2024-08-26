import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

T=int(input())

def dfs(field,x,y,visited):
    visited[y][x]=True
    for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
        nx,ny=x+dx,y+dy

        if 0<=nx<m and 0<=ny<n and not visited[ny][nx] and field[ny][nx]==1:
            dfs(field,nx,ny,visited)

for _ in range(T):
    m,n,k=map(int,input().split())
    field=[[0]*m for _ in range(n)]
    visited=[[False]*m for _ in range(n)]

    for _ in range(k):
        x,y=map(int,input().split())
        field[y][x]=1
    
    cnt=0
    for i in range(n):
        for j in range(m):
            if field[i][j]==1 and not visited[i][j]:
                dfs(field,j,i,visited)
                cnt+=1

    print(cnt)