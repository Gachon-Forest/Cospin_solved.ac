N=int(input())
A=list(map(int,input().split()))
dp=[1]*(len(A))


for i in range(1,len(A)):
    for j in range(i):
        if A[i]>A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))