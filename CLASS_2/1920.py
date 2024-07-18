import sys

N=int(input())
A=list(map(int,sys.stdin.readline().split()))


M=int(input())
nums=list(map(int,sys.stdin.readline().split()))

for i in nums:
    if i in A:
        print('1')
    else:
        print('0')