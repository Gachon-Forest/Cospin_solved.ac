import sys
sys.setrecursionlimit(10000)
def monochrome(x,y,l):
    std = mat[x][y]
    for i in range(x,x+l):
        for j in range(y,y+l):
            if mat[i][j] != std:
                return False
    return True

def papercount(x,y,l):
    global white, blue
    if monochrome(x,y,l):
        if mat[x][y]==0:
            white+=1
        else:
            blue+=1
    else:
        half=l//2
        papercount(x,y,half)
        papercount(x,y+half,half)
        papercount(x+half,y,half)
        papercount(x+half,y+half,half)

n=int(input())
mat=[]
white=0
blue=0

for _ in range(n):
    row=list(map(int,input().split()))
    mat.append(row)

papercount(0,0,n)
print(white)
print(blue)