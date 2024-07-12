n,ltr = map(int,input().split())
num = [i for i in range(1, n+1)]

idx = 0
permutation = []
while len(num) != 0:
    idx+=ltr

    target = num[idx-1]
    permutation.append(target)
print(permutation)