#17281 야구
import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
inning = []
for i in range(n):
    inning.append(list(map(int, input().split())))
player = [i for i in range(1, 9)]
answer = -1
for p in list(permutations(player, 8)):
    p = list(p)
    p.insert(3, 0)
    score = 0
    idx = 0
    for j in range(n):
        base1, base2, base3 = 0, 0, 0
        out = 0
        while True:
            if out == 3:
                break
            if inning[j][p[idx]] == 4:
                score += (base1+base2+base3+1)
                base1, base2, base3 = 0, 0, 0
            elif inning[j][p[idx]] == 3:
                score += (base1+base2+base3)
                base1, base2, base3 = 0, 0, 1
            elif inning[j][p[idx]] == 2:
                score += (base2+base3)
                base1, base2, base3 = 0, 1, base1
            elif inning[j][p[idx]] == 1:
                score += base3
                base1, base2, base3 = 1, base1, base2
            elif inning[j][p[idx]] == 0:
                out += 1
            idx += 1
            idx = idx%9
    answer = max(answer, score)
print(answer)
