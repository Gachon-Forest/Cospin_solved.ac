n=int(input())
tri=[[]]

for _ in range(n):
    tri.append(list(map(int,input().split())))

for i in range(n,0,-1):
    for j in range(len(tri[i-1])):
        tri[i-1][j]+=max(tri[i][j],tri[i][j+1])

print(tri[1][0])