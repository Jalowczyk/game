def handle_user_decision():
    user_decision_height = int(input("Pick height: "))
    user_decision_height += 2
    user_decision_width = int(input("Pick width: "))
    user_decision_width += 2

    return user_decision_height, user_decision_width

def create_board(width, height):

    board = []
    row1 = []
    row2 = []
    #rows preparing
    for i in range(width):
        row1.append("X")

    row2.append("X")
    for i in range(width-2):
        row2.append("-")
    row2.append("X")

    #board preparing
    board.append(row1)

    for i in range(height-2):
        board.append(row2)

    board.append(row1)

    return board


def print_board(board):

    for row in board:
        print(*row)


def main():
    width, height = handle_user_decision()
    board = create_board(width, height)
    print_board(board)
    #board = insert_player(board, 1, 1)

main()
