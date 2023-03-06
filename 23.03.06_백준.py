#1107 리모컨
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
bb = list(map(str, input().split()))
answer = abs(100-n)
for i in range(1000001):
    for j in str(i):
        if j in bb:
            break
        else:
            answer = min(answer, len(str(i))+abs(i-n))

#1987 알파벳
import sys
input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(graph):
    q = set([(0, 0, graph[0][0])])
    answer = 1
    while q:
        x, y, alphabet = q.pop()
        answer = max(answer, len(alphabet))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] not in alphabet:
                    q.add((nx, ny, alphabet+graph[nx][ny]))
    return answer
n, m = map(int, input().split())
graph = []
alphabet = []
for i in range(n):
    graph.append(list(str(input().rstrip())))
visited = [[0]*m for _ in range(n)]
res = bfs(graph)
print(res)