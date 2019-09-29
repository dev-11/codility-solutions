def solution(A, B):
    alive_fish = []
    for _ in range(len(A)):
        if len(alive_fish) == 0:
            alive_fish.append(_)
        else:
            while len(alive_fish) != 0 \
            and B[_] - B[alive_fish[-1]] == -1 \
            and A[alive_fish[-1]] < A[_]:
                alive_fish.pop()

            if len(alive_fish) == 0 or B[_] - B[alive_fish[-1]] != -1:
                alive_fish.append(_)

    return len(alive_fish)

