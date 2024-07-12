N = int(input())

dic = {}
solves = []
for i in range(N):
    string = input()
    if len(string) not in dic.keys():
        dic[len(string)] = [string]
    else:
        dic[len(string)].append(string)

print(dic.items())
for key,value in sorted(dic.items()):
    set(value)
    value.sort()
    for x in value:
        solves.append(x)

# for a in solves:
#     print(a)