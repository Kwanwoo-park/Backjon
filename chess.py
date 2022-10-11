piece = [1, 1, 2, 2, 2, 8]

input_piece = list(map(int, input().split()))

for i, j in zip(piece, input_piece):
    print(i-j, end= ' ')
print()