from z3 import *

f = open("sudoku.txt", "r")
fLines = f.readlines()
board = []
symbolicBoard = []
outBoard = []
s = Solver()
for line in fLines:
  board.append(line.rstrip().split(","))

for i in range(0, len(board)):
  symbolicRow = []
  for j in range (0, len(board[i])):
    symbolicRow.append(Int('x_' + str(i) + '_' + str(j)))
    s.add(symbolicRow[j] > 0, symbolicRow[j] < 10)
    if int(board[i][j]) != 0:
      s.add(symbolicRow[j] == int(board[i][j]))
  symbolicBoard.append(symbolicRow)

#Distinct rows
for i in symbolicBoard:
  s.add(Distinct(*i))

#Distinct Columns
for i in range(0, len(symbolicBoard)):
  s.add(Distinct(*[row[i] for row in symbolicBoard]))

#Distinct sub boxes
numSquares = int(math.sqrt(len(symbolicBoard)))
for i in range(0, numSquares):
  for j in range(0, numSquares):
    symbolicSquare = []
    for k in range(i * numSquares, i * numSquares + numSquares):
      for l in range(j * numSquares, j * numSquares + numSquares):
        symbolicSquare.append(symbolicBoard[k][l])
    s.add(Distinct(*symbolicSquare))

#check and print model if exists
if (s.check()):
  m = s.model()
  for i in symbolicBoard:
    outRow = []
    for j in i:
      outRow.append(m[j])
    outBoard.append(outRow)
else:
  print("No solution could be found")

print(outBoard)





