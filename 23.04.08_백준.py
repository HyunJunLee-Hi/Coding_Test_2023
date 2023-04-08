#연속된 부분 수열의 합
def solution(sequence, k):
    answer = []
    n = len(sequence)
    end = 0
    max_sum = 0

    for i in range(n):
        while max_sum < k and end < n:
            max_sum += sequence[end]
            end += 1
        if max_sum == k:
            answer.append([i, end - 1, end - 1 - i])
        max_sum -= sequence[i]

    answer.sort(key=lambda x: x[2])

    return answer[0][:2]

print(solution([1, 2, 3, 4, 5], 7))

# def solution(sequence, k):
#     answer = []
#     n = len(sequence)
#     for i in range(1, n+1):
#         for j in range(n-i+1):
#             temp = sum(sequence[j:j+i])
#             if temp == k:
#                 answer.append(j)
#                 answer.append(j+i-1)
#                 return answer


#     # return answer