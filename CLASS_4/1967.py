n=int(input())
tree=[[] for _ in range(n+1)]

def dfs(start,tree):
    stack=[(start,0)]
    dist=[-1]*len(tree)
    dist[start]=0
    farthest_node=start
    max_dist=0

    while stack:
        current_node,curent_dist=stack.pop()

        for next,weight in tree[current_node]:
            if dist[next]==-1:
                dist[next]=curent_dist+weight
                stack.append((next,dist[next]))
                if dist[next]>max_dist:
                    max_dist=dist[next]
                    farthest_node=next
    return farthest_node,max_dist

for _ in range(n-1):
    u,v,w=map(int,input().split())
    tree[u].append((v,w))
    tree[v].append((u,w))

vertex1,_=dfs(1,tree)
vertex2,diameter=dfs(vertex1,tree)
print(diameter)