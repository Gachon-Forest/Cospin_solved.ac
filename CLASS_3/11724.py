import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

def dfs(graph,v,visited):
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt=0
visited=[False]*(n+1)

for i in range(1,n+1):
    if not visited[i]:
        dfs(graph,i,visited)
        cnt+=1

print(cnt)