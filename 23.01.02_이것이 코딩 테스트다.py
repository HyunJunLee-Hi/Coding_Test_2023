import sys
input = sys.stdin.readline

#Implementation
## 왕실의 나이트
dx = [-1, 1, -2, 2, -2, 2, -1, 1]
dy = [-2, -2, -1, -1, 1, 1, 2, 2]

answer = 0
cur = input()
col = int(cur[1]) - 1
row = int(ord(cur[0]) - ord('a'))

for i in range(8):
    nx = row + dx[i]
    ny = col + dy[i]
    if 0 <= nx < 8 and 0 <= ny < 8:
        answer += 1

print(answer)

## 게임 개발
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
x, y, d = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
graph[x][y] = 2
answer = 1
chk = 0
while True:
    chk += 1
    d = (d-1)%4
    nx = x + dx[d]
    ny = y + dy[d]
    if 0 <= nx < n and 0 <= ny < m:
        if graph[nx][ny] == 0:
            x, y = nx, ny
            graph[nx][ny] = 2
            chk = 0
            answer += 1
    if chk >= 4:
        if graph[x - dx[d]][y - dy[d]] == 2:
            x = x - dx[d]
            y = y - dy[d]
        else:
            break

print(answer)

# DFS/BFS
## 음료수 얼려 먹기
def dfs(graph, visited, x, y):
    stack = []
    stack.append([x, y])
    graph[x][y] = 2
    visited[x][y] = 1
    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    graph[nx][ny] = 2
                    stack.append([nx, ny])

answer = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())
graph = []
visited = [[0]*m for _ in range(n)]
for i in range(n):
    temp = list(map(int, str(input().strip())))
    graph.append(temp)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            answer += 1
            dfs(graph, visited, i, j)

print(answer)


## 미로 탈출
from collections import deque
def bfs(graph, start):
    q = deque()
    q.append(start)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append([nx, ny])


answer = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, input().split())
graph = []
for i in range(n):
    temp = list(map(int, str(input().strip())))
    graph.append(temp)

bfs(graph, [0, 0])
print(graph[n-1][m-1])
