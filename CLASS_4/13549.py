from collections import deque

def bfs(n,k):
    max_position=100000
    visited=[-1]*(max_position+1)

    queue=deque([n])
    visited[n]=0

    while queue:
        current=queue.popleft()

        if current==k:
            return visited[current]

        if 0<=current*2<=max_position and visited[current*2]==-1:
            visited[current*2]=visited[current]
            queue.appendleft(current*2)

        for next in (current-1,current+1):
            if 0<=next<=max_position and visited[next]==-1:
                visited[next]=visited[current]+1
                queue.append(next)


n,k=map(int,input().split())

print(bfs(n,k))