from collections import deque


def solution(S):
    opening = ['{', '[', '(']
    closing = ['}', ']', ')']
    q = deque()
    for _ in S:
        if _ in opening:
            q.append(_)
        elif _ in closing:
            if len(q) == 0:
                return 0
            bracket = q.pop()
            index_1 = opening.index(bracket)
            index_2 = closing.index(_)

            if index_1 != index_2:
                return 0

    return int(len(q) == 0)

