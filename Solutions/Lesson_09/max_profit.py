import sys


def solution(A):
    prev_min_share = sys.maxsize
    max_profit = 0
    for share in A:
        prev_min_share = min(prev_min_share, share)
        max_profit = max(max_profit, share - prev_min_share)
    return max_profit


print(solution([23171, 21011, 21123, 21366, 21013, 21367]))

#A = [23171, 21011, 21123, 21366, 21013, 21367]

