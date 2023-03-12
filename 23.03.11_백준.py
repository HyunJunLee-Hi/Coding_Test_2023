#17406 배열 돌리기 4
import sys
import copy
from itertools import permutations
input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = []
rcs = []
answer = 9999999999
for i in range(n):
    graph.append(list(map(int, input().split())))
for i in range(k):
    rcs.append(list(map(int, input().split())))
for p in permutations(rcs, k):
    raw = copy.deepcopy(graph)
    for r, c, s in p:
        r, c = r-1, c-1
        temp_graph = copy.deepcopy(raw)
        for j in range(s, 0, -1):
            #R
            # temp_graph[r-j][c-j] = graph[r-j+1][c-j]
            temp_graph[r-j][c-j+1:c+j+1] = raw[r-j][c-j:c+j]
            #L
            # temp_graph[r+j][c+j] = graph[r+j-1][c+j]
            temp_graph[r+j][c-j:c+j] = raw[r+j][c-j+1:c+j+1]
            #U
            for l in range(r-j, r+j):
                temp_graph[l][c-j] = raw[l+1][c-j]
            #D
            for l in range(r-j+1, r+j+1):
                temp_graph[l][c+j] = raw[l-1][c+j]
        raw = temp_graph
    for i in range(n):
        answer = min(answer, sum(raw[i]))
print(answer)