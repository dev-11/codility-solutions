from collections import deque


def solution(A, B):
    alive_fish = []
    for _ in range(len(A)):
        if len(alive_fish) == 0:
            alive_fish.append(_)
        else:
            while len(
                    alive_fish
            ) != 0 and B[_] - B[alive_fish[-1]] == -1 and A[alive_fish[-1]] < A[_]:
                alive_fish.pop()

            if len(alive_fish) == 0:
                alive_fish.append(_)
            elif B[_] - B[alive_fish[-1]] != -1:
                    alive_fish.append(_)

    return len(alive_fish)


A = [0] * 5
B = [0] * 5

A[0] = 4
B[0] = 0
A[1] = 3
B[1] = 1
A[2] = 2
B[2] = 0
A[3] = 1
B[3] = 0
A[4] = 5
B[4] = 0

print(solution(A, B))

