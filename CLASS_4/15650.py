n,m=map(int,input().split())

def btk(n,m,start,current):
    if len(current)==m:
        print(' '.join(map(str,current)))
        return
    
    for i in range(start,n+1):
        current.append(i)
        btk(n,m,i+1,current)
        current.pop()

btk(n,m,1,[])