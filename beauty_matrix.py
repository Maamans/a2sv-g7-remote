# Read the 5x5 matrix and find the position of 1
for i in range(5):
    row = list(map(int, input().split()))
    if 1 in row:
        r = i       # row index of 1 (0-based)
        c = row.index(1)  # column index of 1 (0-based)

# Compute minimum moves to center (2,2) in 0-based indexing
moves = abs(r - 2) + abs(c - 2)
print(moves)