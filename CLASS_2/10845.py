def push(integer):
    queue.append(int(integer))
def pop():
    if not queue:
        results.append(-1)
    else:
        results.append(queue.pop(0))
def size():
    results.append(len(queue))
def empty():
    results.append(1 if not queue else 0)
def front():
    if not queue:
        results.append(-1)
    else:
        results.append(queue[0])
def back():
    if not queue:
        results.append(-1)
    else:
        results.append(queue[-1])

N = int(input())
queue = []
results = []

for _ in range(N):
    term = input().strip()
    if term == 'pop':
        pop()
    elif term == 'size':
        size()
    elif term == 'empty':
        empty()
    elif term == 'front':
        front()
    elif term == 'back':
        back()
    else:
        _, num = term.split()
        push(num)

for result in results:
    print(result)