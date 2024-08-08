N = int(input())
lst = list(map(int,input().split()))
lst.sort()
sum=0
for i in range(len(lst)):
    sum+=lst[i]*(len(lst)-i)

print(sum)