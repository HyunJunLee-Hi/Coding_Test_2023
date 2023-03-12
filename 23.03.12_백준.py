#17070 파이프 옮기기 1
import sys
input = sys.stdin.readline

def dfs(x, y, state):
    global answer
    if x == n-1 and y == n-1:
        answer += 1
        return
    if state == 0:
        if y == n-1:
            return
        if 0 <= x < n and 0 <= y+1 < n and graph[x][y+1] == 0:
            dfs(x, y+1, 0)
        if 0 <= x+1 < n and 0 <= y+1 < n and graph[x][y+1] == 0 and graph[x+1][y] == 0 and graph[x+1][y+1] == 0:
            dfs(x+1, y+1, 2)
    elif state == 1:
        if x == n-1:
            return
        if 0 <= x+1 < n and 0 <= y < n and graph[x+1][y] == 0:
            dfs(x+1, y, 1)
        if 0 <= x+1 < n and 0 <= y+1 < n and graph[x][y+1] == 0 and graph[x+1][y] == 0 and graph[x+1][y+1] == 0:
            dfs(x+1, y+1, 2)
    elif state == 2:
        if 0 <= x < n and 0 <= y+1 < n and graph[x][y+1] == 0:
            dfs(x, y+1, 0)
        if 0 <= x+1 < n and 0 <= y < n and graph[x+1][y] == 0:
            dfs(x+1, y, 1)
        if 0 <= x+1 < n and 0 <= y+1 < n and graph[x][y+1] == 0 and graph[x+1][y] == 0 and graph[x+1][y+1] == 0:
            dfs(x+1, y+1, 2)


n = int(input())
graph = []
answer = 0
for i in range(n):
    graph.append(list(map(int, input().split())))
dfs(0, 1, 0)
print(answer)


import sys
input = sys.stdin.readline

n = int(input())
graph = []
answer = 0
for i in range(n):
    graph.append(list(map(int, input().split())))
dp = [[[0 for i in range(n)] for _ in range(n)] for _ in range(3)]
dp[0][0][1] = 1
for i in range(2, n):
    if graph[0][i] == 0:
        dp[0][0][i] = dp[0][0][i-1]

for i in range(1, n):
    for j in range(1, n):
        if graph[i][j] == 0 and graph[i][j-1] == 0 and graph[i-1][j] == 0:
            dp[2][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]
        if graph[i][j] == 0:
            dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1]
            dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j]
print(dp[0][n-1][n-1]+dp[1][n-1][n-1]+dp[2][n-1][n-1])