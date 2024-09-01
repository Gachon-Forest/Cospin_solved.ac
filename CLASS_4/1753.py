import heapq
import sys
input=sys.stdin.readline

INF=float('inf')

V,E=map(int,input().split())
k=int(input())
graph=[[] for _ in range(V+1)]
dist=[INF]*(V+1)
dist[k]=0

for _ in range(E):
    u,v,w=map(int,input().split())
    graph[u].append((v,w))

queue=[]
heapq.heappush(queue,(0,k))

while queue:
    current_dist,u=heapq.heappop(queue)
    if current_dist>dist[u]:
        continue

    for v,w in graph[u]:
        check=current_dist+w

        if check<dist[v]:
            dist[v]=check
            heapq.heappush(queue,(check,v))

for i in range(1,V+1):
    if dist[i]==INF:
        print("INF")
    else:
        print(dist[i])
