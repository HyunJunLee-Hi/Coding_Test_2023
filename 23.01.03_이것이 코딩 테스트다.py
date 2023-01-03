import sys
input = sys.stdin.readline

# 이진 탐색
## 부품 찾기
def binary_search(lst, x, start, end):
    while start <= end:
        mid = (start+end)//2
        if lst[mid] == x:
            return mid
        elif lst[mid] < x:
            start = mid + 1
        else:
            end = mid - 1

    return False

n = int(input())
lst = list(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))

lst.sort()

for x in target:
    res = binary_search(lst, x, 0, n-1)
    if res == False:
        print("no", end = ' ')
    else:
        print("yes", end = ' ')

## 떡볶이 떡 만들기
n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
start = 0
end = lst[-1]
answer = 0
while start <= end:
    mid = (start+end)//2
    total = 0
    for i in lst:
        if i >= mid:
            total += i-mid
    if total >= m:
        answer = mid
        start = mid + 1
    elif total < m:
        end = mid - 1

print(answer)

# Dynamic Programming
## 1로 만들기
x = int(input())
d = [0] * 300001

for i in range(2, x+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    elif i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    elif i % 5 == 0:
        d[i] = min(d[i], d[i//5]+1)
print(d[x])

## 개미 전사
n = int(input())
lst = list(map(int, input().split()))
d = [0]*101
d[0] = lst[0]
d[1] = max(lst[0], lst[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+lst[i])

print(d[n-1])

## 바닥 공사
n = int(input())
d = [0] * 1001
d[1] = 1
d[2] = 3
for i in range(3, n+1):
    d[i] = (d[i-1] + d[i-2]*2)%796796
print(d[n])

## 효율적인 화폐 구성
n, m = map(int, input().split())
coin = []
for i in range(n):
    coin.append(int(input()))
coin.sort()
dp = [10001]*(m+1)
dp[0] = 0
for i in range(n):
    for j in range(coin[i], m+1):
        if dp[j-coin[i]] != 10001:
            dp[j] = min(dp[j], dp[j-coin[i]] + 1)
if dp[m] != 10001:
    print(dp[m])
else:
    print(-1)

DFS/BFS
# 특정 거리의 도시 찾기
from collections import deque
def bfs(graph, start, n, k):
    visited = [[0]*n for _ in range(n)]
    q = deque()
    q.append([start, start])
    visited[start][start] = 0
    res = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                    # visited[nx][ny] = min(visited[nx][ny], visited[x][y]+1)
                    visited[nx][ny] = visited[x][y] + 1
                    if visited[nx][ny] == k:
                        res += 1
                    q.append([nx, ny])
                    print(visited)
    # for i in range(n):
    #     for j in range(n):
    #         if visited[i][j] == k:
    #             res += 1
    return res




dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m, k, x = map(int, input().split())
graph = [[0]*n for _ in range(n)]
node = [[] for _ in range(n+1)]
x -= 1
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a][b] = 1
    node[a].append(b)

print(bfs(graph, x, n, k))

from collections import deque
n, m, k, x = map(int, input().split())
x -= 1
graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
visited = [-1]*n
visited[x] = 0
q = deque()
q.append(x)
while q:
    a = q.popleft()
    for node in graph[a]:
        if visited[node] == -1:
            visited[node] = visited[a] + 1
            q.append(node)

flag = 0
for i in range(n):
    if visited[i] == k:
        print(i+1)
        flag = 1

if flag == 0:
    print(-1)
