def gcd(a,b):
    for i in range(min(a,b),0,-1):
        if a%i==0 and b%i==0:
            return i

A,B = map(int,input().split())

print(gcd(A,B))
print(int(A*B/gcd(A,B)))