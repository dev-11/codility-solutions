from collections import deque


def solution(S):
    opening = '('
    closing = ')'
    q = deque()
    for _ in S:
        if _ == opening:
            q.append(_)
        elif _ == closing:
            if len(q) == 0:
                return 0
            bracket = q.pop()

    return int(len(q) == 0)

