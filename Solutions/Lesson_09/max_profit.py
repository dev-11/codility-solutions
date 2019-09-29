import sys


def solution(A):
    prev_min_share = sys.maxsize
    max_profit = 0
    for share in A:
        prev_min_share = min(prev_min_share, share)
        max_profit = max(max_profit, share - prev_min_share)
    return max_profit

