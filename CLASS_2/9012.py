N = int(input())

for _ in range(N):
    cnt = 0
    balanced = True
    for br in input():
        if br == '(':
            cnt += 1
        elif br == ')':
            cnt -= 1
        if cnt < 0:
            balanced = False
            break
    if balanced and cnt == 0:
        print('YES')
    else:
        print('NO')