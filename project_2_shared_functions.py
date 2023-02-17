import connectfour

game = connectfour


'''Show user the game display'''

def board_display():

    for counts in range(1, game.BOARD_COLUMNS+1):
        print(counts, end = ' ')
        
    board_game = game.new_game().board
    board_game = [list(row) for row in zip(*(board_game))]

    for i in board_game:
        print()
        for p in i:
            print(p, end= ' ' )

    print()


'''player Red will drop their piece into the column desired first'''

def first_turn(column):

    for counts in range(1, game.BOARD_COLUMNS + 1):
        print(counts,end=' ')
        
    board_game = game.drop(game.new_game(), column-1).board
        
    
    ui_board = [list(row) for row in zip(*(board_game))]

    for i in ui_board:
        print()
        for j in i:
            print(j,end = ' ')

    print()
            
    return (ui_board, board_game)



'''player Yellow will drop their piece into the column desired second'''

def second_turn(user_board, program_board, column):

    second = game.drop(game.GameState(program_board, game.YELLOW), column - 1)
    
    for counts in range(1, game.BOARD_COLUMNS + 1):
        print(counts,end=' ')
        
    board_game = second.board
    ui_board = [list(row) for row in zip(*(board_game))]

    for i in ui_board:
        print()
        for j in i:
            print(j,end = ' ')
    print()
            
    return (ui_board, board_game)


'''If player Yellow chose to drop their game piece, dropped piece will display after column to drop in is chosen'''

def yellow_drop(user_board, program_board, column):


    y_dropped = game.drop(game.GameState(program_board, game.YELLOW), column - 1)
    
    for counts in range(1, game.BOARD_COLUMNS + 1):
        print(counts,end=' ')
        
    board_game = y_dropped.board
    ui_board = [list(row) for row in zip(*(board_game))]

    for i in ui_board:
        print()
        for j in i:
            print(j,end = ' ')
    print()
    
    try:        
        if game.winner(game.GameState(board_game, game.YELLOW)) == 2:
            raise game.GameOverError
        return (ui_board, board_game)

    except game.GameOverError:
        print('\nYELLOW WINS!')
    


'''If player Yellow chose to pop their game piece, the popped piece will display after column to pop from is chosen'''

def yellow_pop(user_board, program_board, column):

    
    y_popped = game.pop(game.GameState(program_board, game.YELLOW), column - 1)
    
    for counts in range(1, game.BOARD_COLUMNS + 1):
        print(counts,end=' ')
        
    board_game = y_popped.board
    ui_board = [list(row) for row in zip(*(board_game))]

    for i in ui_board:
        print()
        for j in i:
            print(j,end = ' ')

    print()
    try:
        if game.winner(game.GameState(board_game, game.YELLOW)) == 2:
            raise game.GameOverError
        return (ui_board, board_game)

    except game.GameOverError:
        print('\nYELLOW WINS!')
            
   

'''If player Red chose to drop their game piece, dropped piece will display after column to drop in is chosen'''

def red_drop(user_board, program_board, column):

    r_dropped = game.drop(game.GameState(program_board, game.RED), column- 1)
    
    for counts in range(1, game.BOARD_COLUMNS + 1):
        print(counts,end=' ')
        
    board_game = r_dropped.board
    ui_board = [list(row) for row in zip(*(board_game))]

    for i in ui_board:
        print()
        for j in i:
            print(j,end = ' ')

    print()
    try:        
        if game.winner(game.GameState(board_game, game.RED)) == 1:
            raise game.GameOverError
        return (ui_board, board_game)
        
    except game.GameOverError:
        print('\nRED WINS!')
        return 
    
    


'''If player Red chose to pop their game piece, the popped piece will display after column to pop from is chosen'''

def red_pop(user_board, program_board, column):

    r_popped = game.pop(game.GameState(program_board, game.RED), column - 1)
    
    for counts in range(1, game.BOARD_COLUMNS + 1):
        print(counts,end=' ')
        
    board_game = r_popped.board
    ui_board = [list(row) for row in zip(*(board_game))]

    for i in ui_board:
        print()
        for j in i:
            print(j,end = ' ')

    print()
    
    try:        
        if game.winner(game.GameState(board_game, game.RED)) == 1:
            raise game.GameOverError
        return (ui_board, board_game)
        
    except game.GameOverError:
        print('\nRED WINS!')
        return
            
    return (ui_board, board_game)






