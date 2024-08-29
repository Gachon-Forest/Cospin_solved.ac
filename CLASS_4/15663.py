def backtrack(depth,path):
    if depth==M:
        print(' '.join(map(str, path)))
        return
    
    last_used=-1
    for i in range(N):
        if not visited[i] and last_used!=numbers[i]:
            visited[i]=True
            backtrack(depth+1,path+[numbers[i]])
            visited[i]=False
            last_used=numbers[i]

N,M=map(int,input().split())
numbers = list(map(int,input().split()))
numbers.sort()
visited=[False]*N

backtrack(0,[])