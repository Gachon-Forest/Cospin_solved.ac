N = int(input())

solves = []
for i in range(N):
    solves.append(input())
    
real_solves = list(set(solves))
real_solves.sort()
real_solves.sort(key=len)
for i in real_solves:
    print(i)