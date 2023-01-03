#징검다리 건너기
import copy
def solution(stones, k):
    answer = 0
    left = 1
    right = max(stones)
    n = len(stones)
    temp_stones = copy.deepcopy(stones)

    while left <= right:
        mid = (left + right) // 2
        for i in range(n):
            temp = stones[i] - mid + 1
            if temp > 0:
                stones[i] = temp
            else:
                stones[i] = 0

        cnt = 0
        for i in range(n):
            if stones[i] == 0:
                cnt += 1
            else:
                cnt = 0
            if cnt == k:
                break

        stones = copy.deepcopy(temp_stones)

        if cnt < k:
            answer = max(answer, mid)
            left = mid + 1
        else:
            right = mid - 1

    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))