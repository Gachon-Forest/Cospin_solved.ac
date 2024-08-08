c=int(input())
n=int(input())
graph = [[] for i in range(c+1)]
visited=[0]*(c+1)

for i in range(n):
    a,b=map(int,input().split())
    graph[a]+=[b]
    graph[b]+=[a]

def dfs(n):
    visited[n]=1
    for nx in graph[n]:
        if visited[nx]==0:
            dfs(nx)

dfs(1)
print(sum(visited)-1)