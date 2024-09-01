import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start,graph,n):
    distance=[INF]*(n+1)
    distance[start]=0
    queue=[(0,start)]
    
    while queue:
        dist,node=heapq.heappop(queue)
        
        if distance[node]<dist:
            continue
        
        for next_node,weight in graph[node]:
            cost=dist+weight
            if cost<distance[next_node]:
                distance[next_node]=cost
                heapq.heappush(queue,(cost,next_node))
    
    return distance


n,m,x=map(int,input().split())

graph=[[] for _ in range(n+1)]
reverse_graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b,t=map(int,input().split())
    graph[a].append((b,t))
    reverse_graph[b].append((a,t))

to_party=dijkstra(x,graph,n)
from_party=dijkstra(x,reverse_graph,n)
max_time=0

for i in range(1,n+1):
    if to_party[i]!=INF and from_party[i]!=INF:
        max_time=max(max_time,to_party[i]+from_party[i])

print(max_time)