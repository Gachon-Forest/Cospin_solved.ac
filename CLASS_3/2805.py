T,m=map(int,input().split())
Trees=list(map(int,input().split()))

def binary_search(start,end):
    while start<=end:
        mid=(start+end)//2
        amp=[i-mid for i in Trees]
        amp=[j for j in amp if j>0]
        total=sum(amp)

        if total==m:
            return mid
        elif total<m:
            end=mid-1
        else:
            start=mid+1

    return end

print(binary_search(0,max(Trees)))