#20920
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
my_dict = {}

for i in range(n):
    word = input().rstrip()
    if len(word) >= m:
        if word in my_dict.keys():
            my_dict[word][0] += 1
        else:
            my_dict[word] = [1, len(word)]
sorted_dict = dict(sorted(my_dict.items(), key = lambda x : (-x[1][0], -x[1][1], x[0])))
for key, value in sorted_dict.items():
    print(key)


#1260
from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    q = deque()
    q.append(v)
    visited = [0] * n
    visited[v] = 1
    res = [v+1]
    while q:
        node = q.popleft()
        for i in range(n):
            if graph[node][i] == 1 and not visited[i]:
                q.append(i)
                res.append(i+1)
                visited[i] = 1
    return res
def dfs(v):
    stack = [v]
    visited = [0]*n
    visited[v] = 1
    res = [v+1]
    while stack:
        node = stack[-1]
        for i in range(n):
            if graph[node][i] == 1 and not visited[i]:
                stack.append(i)
                res.append(i+1)
                visited[i] = True
                break

        else:
            stack.pop()
    return res

n, m, v = map(int, input().split())
v = v-1
graph = [[0]*n for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a = a-1
    b = b-1
    graph[a][b] = 1
    graph[b][a] = 1

answer1 = dfs(v)
answer2 = bfs(v)
print(' '.join(map(str, answer1)))
print(' '.join(map(str, answer2)))