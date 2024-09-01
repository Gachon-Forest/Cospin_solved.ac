import sys
input = sys.stdin.readline

def bellman_ford():
    for i in range(n):
            for j in range(len(edges)):
                current,next,cost=edges[j]
                if dist[next]>dist[current]+cost:
                        dist[next]=dist[current]+cost
                        if i==n-1:
                            return True
    return False

tc=int(input())

for _ in range(tc):
    n,m,w=map(int,input().split())
    edges=[]
    dist=[1e9]*(n+1)
    for i in range(m+w):    
            s,e,t=map(int,input().split())
            if i>=m:
                t=-t
            else:
                edges.append((e,s,t))
            edges.append((s,e,t))
    if bellman_ford():
            print("YES")
    else:
            print("NO")