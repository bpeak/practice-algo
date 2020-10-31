DIRECTION_TOP = 0
DIRECTION_RIGHT = 1
DIRECTION_BOTTOM = 2
DIRECTION_LEFT = 3

def solution(matrix, y, x, direction):
    # 현재위치
    curr_x = x
    curr_y = y

    visited = set()
    visited.add((curr_y, curr_x))    

    while True:
        for i in range(4):
            # -90도 회전
            direction -= 1
            if direction == -1:
                direction = DIRECTION_LEFT

            temp_x = curr_x
            temp_y = curr_y
            if direction == DIRECTION_TOP:
                temp_y -= 1
            elif direction == DIRECTION_RIGHT:
                temp_x += 1
            elif direction == DIRECTION_BOTTOM:
                temp_y += 1
            elif direction == DIRECTION_LEFT:
                temp_x -= 1
            
            if temp_y >= 0 and \
                temp_y <= len(matrix) - 1 and \
                temp_x >= 0 and \
                temp_x <= len(matrix[0]) - 1 and \
                matrix[temp_y][temp_x] == 0 and \
                (temp_y, temp_x) not in visited:
                    # 이동
                    curr_x = temp_x
                    curr_y = temp_y
                    visited.add((curr_y, curr_x))
                    break
        else:
            # 뒤로이동 ( 반대방향 ex>TOP이면 BOTTOM으로 )
            temp_x = curr_x
            temp_y = curr_y
            if direction == DIRECTION_TOP:
                temp_y -= 1
            elif direction == DIRECTION_RIGHT:
                temp_x += 1
            elif direction == DIRECTION_BOTTOM:
                temp_y += 1
            elif direction == DIRECTION_LEFT:
                temp_x -= 1

            if temp_y >= 0 and \
                temp_y <= len(matrix) - 1 and \
                temp_x >= 0 and \
                temp_x <= len(matrix[0]) - 1 and \
                matrix[temp_y][temp_x] == 0:
                    # 이동
                    curr_x = temp_x
                    curr_y = temp_y
                    visited.add((curr_y, curr_x))
            else:
                return len(visited) 

print(solution([
    [1,1,1,1],
    [1,0,0,1],
    [1,1,0,1],
    [1,1,1,1],
], 1, 1, 0))