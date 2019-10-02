def solution(H):
    wall = [None] * len(H)
    wall_position = 0
    used_blocks = 0

    for height in H:
        while wall_position > 0 and wall[wall_position - 1] > height:
            wall_position -= 1
        if wall_position < 1 or wall[wall_position - 1] != height:
            wall[wall_position] = height
            wall_position += 1
            used_blocks += 1

    return used_blocks

