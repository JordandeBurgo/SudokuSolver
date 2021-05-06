def sudoku_solver(sudoku):
    """
    Solves a Sudoku puzzle and returns its unique solution.

    Input
        sudoku : 9x9 numpy array
            Empty cells are designated by 0.

    Output
        9x9 numpy array of integers
            It contains the solution, if there is one. If there is no solution, all array entries should be -1.
    """
    
    global rows,cols,squares,dict_of_dependencies,dict_of_units
    rows = '123456789'
    cols = 'ABCDEFGHI'
    squares = []
    
    for i in rows:
        for j in cols:
            squares.append(j+i)
    
    list_of_affected = []
    this_row = []
    this_col = []
    this_box = []
    for row in rows:
        for col in cols:
            this_row.append(col+row)
        list_of_affected.append(this_row)
        this_row=[]
    for col in cols:
        for row in rows:
            this_col.append(col+row)
        list_of_affected.append(this_col)
        this_col=[]
    for col in ('ABC', 'DEF', 'GHI'):
        for row in ('123', '456', '789'):
            for c in col:
                for r in row:
                    this_box.append(c+r)
            list_of_affected.append(this_box)
            this_box = []
    dict_of_units = dict((square, [affected for affected in list_of_affected if square in affected]) for square in squares)
    dict_of_dependencies = dict((square, set(sum(dict_of_units[square],[])) - set([square])) for square in squares)
    state = generate_board()
    puzzle = dict(zip(squares, sudoku.flatten().tolist()))
    solved_puzzle_dict = dfs(starting_constraints(state, puzzle))
    solved_sudoku = final_solution(solved_puzzle_dict)
    return solved_sudoku

def generate_board():
    return dict((s, rows) for s in squares)

def assign_value_to_square(board, square, value):
    value = str(value)
    elimination = board[square].replace(value,'')
    if all(remove_value_from_square(board, square, val) for val in elimination):
        return board
    return False
    
def remove_value_from_square(board, square, value):
    if value not in board[square]:
        return board
    board[square] = board[square].replace(value, '')
    
    if len(board[square])==0:
        return False
    if len(board[square])==1:
        assigned_val = board[square]
        for sq in dict_of_dependencies[square]:
            if not remove_value_from_square(board, sq, assigned_val):
                return False
    for unit in dict_of_units[square]:
        unit_squares = [sq for sq in unit if value in board[sq]]
        if len(unit_squares) == 0:
            return False
        elif len(unit_squares) == 1:
            if not assign_value_to_square(board, unit_squares[0], value):
                return False
    return board
        
def starting_constraints(board, puzzle):
    for square, value in puzzle.items():
        if str(value) in rows and not assign_value_to_square(board, square, value):
            return False
    return board

def dfs(board):
    if board is False:
        return False
    if all(len(board[square]) == 1 for square in squares):
        return board
    min_vals_left = 10
    for square in squares:
        if len(board[square]) < min_vals_left and len(board[square]) > 1:
            next_square_to_process = square
            min_vals_left = len(board[square])
    
    return get_solution(dfs(assign_value_to_square(board.copy(), next_square_to_process, val)) for val in board[next_square_to_process])
    
def get_solution(results):
    for result in results:
        if result:
            return result
    return False
    
def final_solution(reference_dict):
    solution = []
    line = []
    i = 0
    if reference_dict is False:
        solution = np.full((9, 9), -1)
    else:
        for val in list(reference_dict.values()):
            if i < 9:
                line.append(int(val))
                i+=1
            else:
                solution.append(line)
                line = [int(val)]
                i=1
        solution.append(line)
        solution = np.array(solution)
    return solution
