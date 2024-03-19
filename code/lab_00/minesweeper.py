from random import randrange


def get_number(a, b):
    while True:
        try:
            n = int(input(f"Podaj liczbe calkowita z zakresu {a} - {b}: "))
        except ValueError:
            print("To nie jest liczba calkowita")
        else:
            if a <= n <= b:
                return n
            else:
                print("liczba poza zakresem")


def lay_mines(r, c, number_of_mines):
    mines = set()
    while len(mines) < number_of_mines:
        i = randrange(r)
        j = randrange(c)
        mines.add((i, j))

    return mines


def number_of_neighbouring_mines(square, mines):
    count = 0
    i = square[0]
    j = square[1]

    for x in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
              (i, j - 1), (i, j + 1),
              (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]:
        if x in mines:
            count += 1
    return count


def create_board(r, c, mines, mine='*'):
    board = []
    for i in range(r):
        row = []
        for j in range(c):
            if (i, j) in mines:
                row.append(mine)
            else:
                row.append(number_of_neighbouring_mines((i, j), mines))
        board.append(row)
    return board


def reveal_fields(position, board, r, c, squares):
    i = position[0]
    j = position[1]
    if (i, j) in squares or not (0 <= i < r and 0 <= j < c):
        return
    squares.add((i, j))

    if board[i][j] != 0:
        return
    for p in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
              (i, j - 1), (i, j + 1),
              (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]:
        reveal_fields(p, board, r, c, squares)


def print_board(board, r, c, squares, show_all=False):
    print('   ', end='')
    for j in range(c):
        print(f'{j:^3}', end='')
    print()

    for i in range(r):
        print(f'{i:^3}', end='')
        for j in range(c):
            if show_all or (i, j) in squares:
                print(f'{board[i][j]:^3}', end='')
            else:
                print(f'{'#':^3}', end='')
        print()


r = 10
c = 10
number_of_mines = 3

mines = lay_mines(r, c, number_of_mines)
board = create_board(r, c, mines)
squares = set()  # odkryte pola

while len(squares) < r * c - number_of_mines:
    print_board(board, r, c, squares)
    print(len(squares))
    print("Podaj numer wiersza, ", end='')
    i = get_number(0, r - 1)
    print("Podaj numer kolumny, ", end='')
    j = get_number(0, c - 1)
    if (i, j) in mines:
        print('GAME OVER')
        print_board(board, r, c, squares, True)
        break
    else:
        reveal_fields((i, j), board, r, c, squares)
else:
    reveal_fields((i, j), board, r, c, squares)
    print_board(board, r, c, squares, True)
    print("GG")
