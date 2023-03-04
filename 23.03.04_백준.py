#2573 빙산
import sys
import copy
from collections import deque
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(graph, visited, n, m):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and visited[i][j] == 0:
                q = deque()
                q.append([i, j])
                visited[i][j] = 1
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < m:
                            if graph[nx][ny] != 0 and visited[nx][ny] == 0:
                                visited[nx][ny] = 1
                                q.append([nx, ny])
                cnt += 1

    return cnt


def melting(graph, n, m):
    temp_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            cnt = 0
            if graph[i][j] != 0:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if graph[nx][ny] == 0:
                        cnt += 1
            temp_graph[i][j] -= cnt
            if temp_graph[i][j] < 0:
                temp_graph[i][j] = 0

    return temp_graph

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

answer = 0
while True:
    visited = [[0]*m for _ in range(n)]
    chk = bfs(graph, visited, n, m)
    if chk > 1:
        print(answer)
        break
    if chk == 0:
        print(0)
        break
    graph = melting(graph, n, m)
    answer += 1
