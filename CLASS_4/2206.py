from collections import deque

def bfs(n,m,graph):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    visited=[[[0]*2 for _ in range(m)] for _ in range(n)]
    
    queue=deque([(0,0,0)])
    visited[0][0][0]=1
    
    while queue:
        x,y,wall=queue.popleft()
        
        if x==n-1 and y==m-1:
            return visited[x][y][wall]
        
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==0 and visited[nx][ny][wall]==0:
                    visited[nx][ny][wall]=visited[x][y][wall]+1
                    queue.append((nx,ny,wall))
                
                if graph[nx][ny]==1 and wall==0 and visited[nx][ny][1]==0:
                    visited[nx][ny][1]=visited[x][y][wall]+1
                    queue.append((nx,ny,1))
    return -1

n,m=map(int,input().split())
graph=[list(map(int,input().strip())) for _ in range(n)]

print(bfs(n,m,graph))
