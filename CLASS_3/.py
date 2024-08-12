from collections import deque

m, n = map(int, input().split())
box = []
queue = deque()

# 입력과 동시에 익은 토마토의 위치를 큐에 삽입
for i in range(n):
    row = list(map(int, input().split()))
    box.append(row)
    for j in range(m):
        if row[j] == 1:
            queue.append((i, j))

moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

while queue:
    x, y = queue.popleft()

    for dx, dy in moves:
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
            box[nx][ny] = box[x][y] + 1
            queue.append((nx, ny))

# 결과 계산
result = 0
for row in box:
    for val in row:
        if val == 0:  # 익지 않은 토마토가 남아있으면 -1 출력
            print(-1)
            exit()
        result = max(result, val)

print(result - 1)  # 첫 날을 1로 시작했으므로 최종 결과에서 1을 뺀다.