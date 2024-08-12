N,r,c=map(int,input().split())
quadrant=[]
sum=0
def rec(n,r,c):
    if n==0:
        return True
    if r>=n and c>=n:
        quadrant.append(3)
        rec(n//2,r-n,c-n)
    elif r>=n and c<n:
        quadrant.append(2)
        rec(n//2,r-n,c)
    elif r<n and c>=n:
        quadrant.append(1)
        rec(n//2,r,c-n)
    else:
        quadrant.append(0)
        rec(n//2,r,c)

rec(2**(N-1),r,c)

fourth=[4**(i-1) for i in range(N,0,-1)]

for j in range(N):
    sum+=(quadrant[j]*fourth[j])

print(sum)