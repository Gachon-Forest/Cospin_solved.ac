import sys
sys.setrecursionlimit(10**6)

N=int(input())
graph=[[] for _ in range(N+1)]
parents=[0]*(N+1)
visited=[False]*(N+1)

for _ in range(N-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(child):
    visited[child]=True

    for node in graph[child]:
        if not visited[node]:
            parents[node]=child
            dfs(node)

dfs(1)

for i in range(2,N+1):
    print(parents[i])