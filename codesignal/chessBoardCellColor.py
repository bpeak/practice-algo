def chessBoardCellColor(cell1, cell2):
    x1, y1 = int(ord(cell1[0]) - 64), int(cell1[1])
    x2, y2 = int(ord(cell2[0]) - 64), int(cell2[1])
    return (abs(x1 - x2) + abs(y1 - y2)) % 2 == 0

print(chessBoardCellColor('A1', 'C3')) # True
print(chessBoardCellColor('A1', 'H3')) # False