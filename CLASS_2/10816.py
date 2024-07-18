N = int(input())
num = list(map(int, input().split()))
M = int(input())
target = list(map(int, input().split()))

num_count = {}

for n in num:
    if n in num_count:
        num_count[n] += 1
    else:
        num_count[n] = 1

result = [num_count.get(t, 0) for t in target]

print(*result)