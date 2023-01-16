import sys
input = sys.stdin.readline

# DFS/BFS
## 경쟁적 전염
from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, k = map(int, input().split())
viruses = []
graph = []
for i in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)
    for j in range(n):
        if temp[j] != 0:
            viruses.append([temp[j], 0, i, j])

viruses.sort()
q = deque(viruses)
s, x, y = map(int, input().split())

while q:
    virus, t, i, j = q.popleft()
    if t == s:
        break
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append([virus, t+1, nx, ny])

print(graph[x-1][y-1])




# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
# n, k = map(int, input().split())
# viruses = [i for i in range(1, k+1)]
# visited = [[0]*n for _ in range(n)]
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input().split())))
# s, x, y = map(int, input().split())
#
# import copy
# for _ in range(s):
#     temp = copy.deepcopy(graph)
#     for virus in viruses:
#         for i in range(n):
#             for j in range(n):
#                 if graph[i][j] == virus:
#                     for k in range(4):
#                         nx = i + dx[k]
#                         ny = j + dy[k]
#                         if 0 <= nx < n and 0 <= ny < n:
#                             if temp[nx][ny] == 0:
#                                 temp[nx][ny] = virus
#     graph = temp
# print(graph[x-1][y-1])







# from collections import deque
# import copy
# # import numpy as np
# def bfs(graph, visited, n, start, virus):
#     q = deque()
#     q.append(start)
#     visited[start[0]][start[1]] = 1
#     # while q:
#     a, b = q.popleft()
#     for i in range(4):
#         nx = a + dx[i]
#         ny = b + dy[i]
#         if 0 <= nx < n and 0 <= ny < n:
#             if graph[nx][ny] == 0 and visited[nx][ny] == 0:
#                 graph[nx][ny] = virus
#                 visited[nx][ny] = 1
#                 # print(np.array(graph))
#                     # q.append([nx, ny])
#     return graph, visited
#
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
# n, k = map(int, input().split())
# viruses = [i for i in range(1, k+1)]
# visited = [[0]*n for _ in range(n)]
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input().split())))
# s, x, y = map(int, input().split())
#
# for _ in range(s):
#     temp = copy.deepcopy(graph)
#     for virus in viruses:
#         for i in range(n):
#             for j in range(n):
#                 if graph[i][j] == virus:
#                     temp, visited = bfs(temp, visited, n, [i, j], virus)
#     graph = temp
#
#     # print(np.array(graph))
# print(graph[x-1][y-1])