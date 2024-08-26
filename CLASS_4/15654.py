import sys
sys.setrecursionlimit(10**6)

n,m=map(int,input().split())
nums=list(map(int,input().split()))
nums.sort()
def btk(n,m,nums,current):
    if len(current)==m:
        print(' '.join(map(str,current)))
        return
    
    for i in range(0,n):
        if nums[i] not in current:
            current.append(nums[i])
            btk(n,m,nums,current)
            current.pop()

btk(n,m,nums,[])