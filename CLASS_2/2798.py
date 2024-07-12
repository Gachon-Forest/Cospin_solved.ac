N, target = map(int,input().split())

lst = list(map(int,input().split()))

de_cards = []

for i in range(len(lst)-2):
    for j in range(i+1,len(lst)-1):
        for k in range(j+1,len(lst)):
            de_cards.append(lst[i]+lst[j]+lst[k])

for index,value in enumerate(de_cards):
    if target - value < 0:
        de_cards[index] = 0

de_cards.sort()

print(de_cards[-1])