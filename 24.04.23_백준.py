#1260
import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    q = deque()
    q.append(v)
    visited = [0]*n
    visited[v] = 1
    res = [v+1]
    while q:
        node = q.popleft()
        for i in range(n):
            if graph[node][i] == 1 and not visited[i]:
                visited[i] = 1
                res.append(i+1)
                q.append(i)

    return res

def dfs(v):
    visited[v] = 1
    for i in range(n):
        if graph[v][i] == 1 and not visited[i]:
            visited[i] = 1
            res.append(i+1)
            dfs(i)

n, m, v = map(int, input().split())
v -= 1
graph = [[0]*n for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a][b] = 1
    graph[b][a] = 1


ans2 = bfs(v)

stack = [v]
visited = [0] * n
visited[v] = 1
res = [v + 1]
dfs(v)
ans1 = res
print(' '.join(map(str, ans1)))
print(' '.join(map(str, ans2)))

#13335
import sys
from collections import deque
input = sys.stdin.readline

n, w, l = map(int, input().split())
q = deque()
res = 0
trucks = deque(map(int, input().split()))
bridge = deque()
for i in range(w):
    bridge.append(0)
while trucks or sum(bridge) != 0:
    if trucks:
        truck = trucks.popleft()
        if sum(bridge) + truck - bridge[0] > l:
            bridge.popleft()
            bridge.append(0)
            trucks.insert(0, truck)
        else:
            bridge.popleft()
            bridge.append(truck)
        res += 1
    else:
        bridge.popleft()
        bridge.append(0)
        res += 1
print(res)
