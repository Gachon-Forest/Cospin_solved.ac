n,m=map(int,input().split())
nums=list(map(int,input().split()))
prefix_sum=[0]*(n+1)

for k in range(1,n+1):
    prefix_sum[k]=prefix_sum[k-1]+nums[k-1]

out=[]
for _ in range(m):
    i,j=map(int,input().split())
    out.append(str(prefix_sum[j]-prefix_sum[i-1]))

print("\n".join(out))