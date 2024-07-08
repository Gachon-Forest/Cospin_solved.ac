N=int(input())


for _ in range(N):
    R = ''
    repeat, string = input().split()

    for i in string:
        for _ in range(int(repeat)):
            R+=i
    print(R)