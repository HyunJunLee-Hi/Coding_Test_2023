# #9017
# import sys
# input = sys.stdin.readline
#
# t = int(input())
# for _ in range(t):
#     n = int(input())
#     score = list(map(int, input().split()))
#     teams = dict()
#     for i in range(n):
#         if score[i] in teams.keys():
#             teams[score[i]].append(i+1)
#             teams[score[i]].sort()
#         else:
#             teams[score[i]] = [i+1]
#
#     for key in teams.keys():
#         if len(teams[key]) < 6:
#             while key in score:
#                 score.remove(key)
#
#     teams = dict()
#     for i in range(len(score)):
#         if score[i] in teams.keys():
#             teams[score[i]].append(i + 1)
#             teams[score[i]].sort()
#         else:
#             teams[score[i]] = [i + 1]
#
#     candidate = -1
#     candidate_score = 1000001
#     candidate_5 = 1000001
#     for key, value in teams.items():
#         if len(teams[key]) >= 6:
#             if candidate_score > sum(teams[key][:4]):
#                 candidate = key
#                 candidate_score = sum(teams[key][:4])
#                 candidate_5 = teams[key][4]
#             elif candidate_score == sum(teams[key][:4]):
#                 if teams[key][4] < candidate_5:
#                     candidate = key
#                     candidate_score = sum(teams[key][:4])
#                     candidate_5 = teams[key][4]
#     print(candidate)
#

#13305
import sys
input = sys.stdin.readline

n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = price[0]
total_price = 0

for i in range(n-1):
    if min_price > price[i]:
        min_price = price[i]
    total_price += min_price*distance[i]

print(total_price)



