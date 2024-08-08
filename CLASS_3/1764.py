n, m = map(int, input().split())
dd = set()
bd = set()

for _ in range(n):
    dd.add(input().strip())
for _ in range(m):
    bd.add(input().strip())

ddbd = sorted(dd & bd)

print(len(ddbd))
for name in ddbd:
    print(name)