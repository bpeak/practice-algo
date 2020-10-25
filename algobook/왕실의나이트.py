def solution(pos):
    col_map = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    x = col_map.index(pos[0]) + 1
    y = int(pos[1])
    directions = ((2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2))
    count = 0
    for dx, dy in directions:
        next_x = x + dx
        next_y = y + dy
        if next_x <= 8 and \
            next_x >= 1 and \
            next_y <= 8 and \
            next_y >= 1:
            count += 1
    return count

print(solution('a1'))
print(solution('c2'))

# cf map없이 아스키테이블 이용해서 x 구하는 방법도 있음
"""
char1 = 'a'
char2 = 'c'
print(ord(char1) - ord('a'))
print(ord(char2) - ord('a'))
"""