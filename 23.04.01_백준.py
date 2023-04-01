#17471 게리맨더링
import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

def is_connected(group):
    q = deque()
    q.append(group[0])
    visited = [0]*n
    visited[group[0]] = 1
    while q:
        x = q.popleft()
        for i in graph[x]:
            if i in group:
                if visited[i] == 0:
                    visited[i] = 1
                    q.append(i)
    if sum(visited) == len(group):
        return True

    return False

n = int(input())
people = list(map(int, input().split()))
graph = [[] for _ in range(n)]
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(1, temp[0]+1):
        graph[i].append(temp[j]-1)

vertex = [i for i in range(n)]
answer = 9999999999

for i in range(1, n//2+1):
    temp = list(combinations(vertex, i))
    for g1 in temp:
        g2 = [j for j in vertex if j not in g1]

        if is_connected(g1) and is_connected(g2):
            num_g1 = 0
            num_g2 = 0
            for j in g1:
                num_g1 += people[j]
            for j in g2:
                num_g2 += people[j]

            answer = min(answer, abs(num_g1-num_g2))

if answer != 9999999999:
    print(answer)
else:
    print(-1)
