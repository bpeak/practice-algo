#me
row, col = list(map(int, input().split(" ")))
for i in range(col):
  print("*" * row)

#best
print(("*" * row + '\n') * col)