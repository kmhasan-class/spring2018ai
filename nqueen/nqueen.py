def get_random_board(n):
    #homework write the body of this function
    #return a random board of size n x n
    board = [1, 0, 2, 2]
    return board


def count_conflicts(board):
    #homework make this function efficient
    n = len(board)
    #for (int i = 0; i < n; i++)
    #    printf("%d %d", i, board[i]);

    row_conflicts = 0
    diag_conflicts = 0
    inv_diag_conflicts = 0

    for i in range(0, n):
        # q1 is queen 1 at (r1, c1)
        r1 = board[i]
        c1 = i
        for j in range(i + 1, n):
            # q2 is queen 2 at (r2, c2)
            r2 = board[j]
            c2 = j
            if r1 == r2:
                row_conflicts += 1
            if r1 - c1 == r2 - c2:
                diag_conflicts += 1
            if r1 + c1 == r2 + c2:
                inv_diag_conflicts += 1

    total_conflicts = row_conflicts + diag_conflicts + inv_diag_conflicts
    #print(row_conflicts, diag_conflicts, inv_diag_conflicts)
    return total_conflicts


def get_next_board(board):
    better_board = []
    least_conflicts = count_conflicts(board)
    for c in range(0, len(board)):
        current_row = board[c]
        for r in range(0, len(board)):
            board[c] = r
            new_conflicts = count_conflicts(board)
            if new_conflicts < least_conflicts:
                least_conflicts = new_conflicts
                better_board = list(board)
            #print("Col: ", c, "Row: ", r, "Conflicts: ", new_conflicts)
        board[c] = current_row
        #print('\n')
    #print(better_board, least_conflicts)
    return better_board, least_conflicts


board = get_random_board(4)

best_board = list(board)
least_conflicts = count_conflicts(best_board)
print("Initial board: ", board, " Conflicts: ", least_conflicts)

while True:
    better_board, conflicts = get_next_board(best_board)
    print("New board:", better_board, " Conflicts: ", conflicts)
    if conflicts < least_conflicts:
        least_conflicts = conflicts
        best_board = list(better_board)
    else:
        #homework modify this part
        #when we get stuck we should restart from a random board
        #make sure you put a fixed count on how many times we do this
        break

print("Best board: ", best_board, " Conflicts: ", least_conflicts)
