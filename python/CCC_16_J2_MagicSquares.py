square = []
sums_row = []
sums_col = []
for i in range(4):
    currentrow = [0,0,0,0]
    square.append(currentrow)
for i in range(4):
    currentline = input().split()
    for j in range(4):
        square[i][j] = int(currentline[j])
for i in range(4):
    csum = 0
    for j in range(4):
        csum += square[i][j]
    sums_row.append(csum)

for i in range(4):
    csum = 0
    for j in range(4):
        csum += square[j][i]
    sums_col.append(csum)

if sums_col[0] == sums_col[1] and sums_col[1] == sums_col[2] and sums_col[2] == sums_col[3]\
   and  sums_row[0] == sums_row[1] and  sums_row[1] == sums_row[2] and  sums_row[2] == sums_row[3]\
   and sums_col[0] == sums_row[0]:
   print("magic")
else:
    print("not magic")
