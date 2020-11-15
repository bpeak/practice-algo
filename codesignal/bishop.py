wmap = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8.
}

directions = ((1, 1), (1, -1), (-1, 1), (-1, -1))

def bishopAndPawn(bishop, pawn):
    b = wmap[bishop[0]], int(bishop[1])
    # b = ord(bishop[0]) - 96, int(bishop[1])
    p = wmap[pawn[0]], int(pawn[1])
    # p = ord(pawn[0]) - 96, int(pawn[1])
    for dx, dy in directions:
        x = b[0]
        y = b[1]
        while True:
            x += dx
            y += dy
            if x > 8 or y > 8 or x < 0 or y < 0:
                break            
            if x == p[0] and y == p[1]:
                return True
    return False

print(bishopAndPawn('a1', 'c3')) # T
print(bishopAndPawn('h1', 'h3')) # F
print(bishopAndPawn('a5', 'c3')) # T
print(bishopAndPawn('g1', 'f3')) # F
print(bishopAndPawn('e7', 'd6')) # T
print(bishopAndPawn('e7', 'a3')) # T