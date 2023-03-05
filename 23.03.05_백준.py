#16236 아기 상어
import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, n, b_x, b_y):
    q = deque()
    q.append([b_x, b_y, 0])
    target = []
    visited = [[0]*n for _ in range(n)]
    visited[b_x][b_y] = 1
    min_d = 9999999999
    while q:
        x, y, d = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    if graph[nx][ny] <= b_shark:
                        if 0 < graph[nx][ny] < b_shark:
                            min_d = d
                            target.append([d+1, nx, ny])
                        if d+1 <= min_d:
                            q.append([nx, ny, d+1])
    if target:
        target.sort()
        return target[0]
    else:
        return False


n = int(input())
graph = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
time = 0
b_shark = 2
fish_num = 0
eat = 0
for i in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)
    for j in range(n):
        if temp[j] == 9:
            b_x, b_y = i, j
        elif 0 < temp[j] < 7:
            fish_num += 1
graph[b_x][b_y] = 0

while fish_num:
    res = bfs(graph, n, b_x, b_y)
    if not res:
        break
    b_x, b_y = res[1], res[2]
    time += res[0]
    eat += 1
    fish_num -= 1
    if b_shark == eat:
        b_shark += 1
        eat = 0
    graph[b_x][b_y] = 0

print(time)