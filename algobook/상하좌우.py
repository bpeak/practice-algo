def solution(N, plans):
    x, y = 1, 1
    for plan in plans:
        next_x, next_y = x, y
        if plan == 'L':
            next_y -= 1
        elif plan == 'R':
            next_y += 1
        elif plan == 'U':
            next_x -= 1
        elif plan == 'D':
            next_x += 1
        if next_x >= 1 and \
            next_x <= N and \
            next_y >= 1 and \
            next_y <= N:
            x = next_x
            y = next_y
    return f'{x} {y}'

print(solution(5, ['R', 'R', 'R', 'U', 'D', 'D']))