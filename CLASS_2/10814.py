N = int(input())
members = {}
for _ in range(N):
    age,name = input().split()
    age = int(age)
    if age not in members.keys():
        members[age] = []
    members[age].append(name)

for age in sorted(members.keys()):
    for name in members[age]:
        print(age, name)
