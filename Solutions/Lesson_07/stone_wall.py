def solution(H):
    wall = [None] * len(H)
    wall_position = 0
    used_blocks = 0

    for _, current_height in enumerate(H):
        while wall_position > 0 and wall[wall_position - 1] > current_height:
            wall_position -= 1
        if wall_position == 0 or wall[wall_position - 1] != current_height:
            wall[wall_position] = current_height
            wall_position += 1
            used_blocks += 1

    return used_blocks


