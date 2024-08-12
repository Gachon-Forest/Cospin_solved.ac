from collections import deque

def bfs(n,k):
    max_position=100000
    visited=[0]*(max_position+1)

    queue=deque([n])
    visited[n]=1

    while queue:
        current=queue.popleft()

        if current==k:
            return visited[current]-1

        for next in (current-1,current+1,current*2):
            if 0<=next<=max_position and not visited[next]:
                visited[next]=visited[current]+1
                queue.append(next)
n,k=map(int,input().split())

print(bfs(n,k))