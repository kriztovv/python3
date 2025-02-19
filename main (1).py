import random

# ukol 1
def create_random_matrix(rows, cols, max_val):
    matrix = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append(random.randint(0, max_val))
        matrix.append(row)
    return matrix

m1 = create_random_matrix(3, 4, 10)
for row in m1:
    print(row)

# ukol 2
def create_chessboard(n):
    board = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append((i + j) % 2)
        board.append(row)
    return board

chess = create_chessboard(8)
for row in chess:
    print(row)

# ukol 3
def swap_rows(matrix, row1, row2):
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]
    return matrix

mat3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
mat3 = swap_rows(mat3, 0, 2)
for row in mat3:
    print(row)

# ukol 4
def print_matrix(matrix):
    col_count = max(len(row) for row in matrix)
    col_widths = []
    for col_index in range(col_count):
        max_len = max(len(str(row[col_index])) for row in matrix)
        col_widths.append(max_len)
    def print_separator():
        print('+', end='')
        for width in col_widths:
            print('-' * width, end='+')
        print()
    print_separator()
    for row in matrix:
        print('|', end='')
        for i, val in enumerate(row):
            print(str(val).rjust(col_widths[i]), end='|')
        print()
        print_separator()

mat4 = [
    [1, 5, 15, -1457, 12],
    [1, 125, 715, 89, 65],
    [17, 95, 816, 30, 132]
]
print_matrix(mat4)

# ukol 5
def align_text(text, width, alignment):
    alignment = alignment.lower()
    if alignment == 'left':
        return text.ljust(width)
    elif alignment == 'right':
        return text.rjust(width)
    elif alignment == 'center':
        return text.center(width)
    else:
        return text

t = "Hello"
print(align_text(t, 10, 'left'))
print(align_text(t, 10, 'right'))
print(align_text(t, 10, 'center'))

# ukol 6
def transpose_matrix(matrix):
    transposed = []
    for row in zip(*matrix):
        transposed.append(list(row))
    return transposed

mat6 = [
    [1, 2, 3],
    [4, 5, 6]
]
tmat6 = transpose_matrix(mat6)
for row in tmat6:
    print(row)
