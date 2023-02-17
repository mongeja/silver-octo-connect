#mongeja 73098617

import connectfour
import project_2_shared_functions as shared

game = connectfour

columns = int(input('Enter columns: '))
rows = int(input('Enter rows: '))

game.BOARD_COLUMNS = columns
game.BOARD_ROWS = rows


'''player Red will drop their piece into the column desired first'''

def first():
    
    try:
        column_to_drop = int(input('\nRED:\nEnter a column number to drop: '))

        boards = shared.first_turn(column_to_drop)

        return second(boards[0], boards[1])
    
    except ValueError:
        print('\nPlease enter a valid integer')
        first()

    except game.InvalidMoveError:
        print('\nPlease enter a valid integer')
        first()
    except game.GameOverError:
        pass


'''player Yellow will drop their piece into the column desired second'''

def second(user_board, program_board):
    ui_board = user_board
    board_game = program_board
    
    try:
        column_to_drop = int(input('\nYELLOW:\nEnter a column number to drop: '))

        boards = shared.second_turn(user_board, program_board, column_to_drop)

        return red(boards[0], boards[1])
    
    except ValueError:
        print('\nPlease enter a valid integer')
        second(ui_board, board_game)
        
    except game.InvalidMoveError:
        print('\nPlease enter a valid integer')
        second(ui_board, board_game)
        
    except game.GameOverError:
        pass
            
'''Take input from player Yellow to either pop or drop a game piece of their own color
    into column of choice'''

def yellow(user_board, program_board):
    ui_board = user_board
    board_game = program_board
    
    try:
        drop_or_pop = input('\nYELLOW:\nWould you like to "pop" or "drop": ')
        if drop_or_pop.lower() == 'drop':
            column = int(input('\nYELLOW:\nEnter a column number to ' + drop_or_pop + ': '))
            boards = shared.yellow_drop(user_board, program_board, column)
            
        elif drop_or_pop.lower() == 'pop':
            column = int(input('\nYELLOW:\nEnter a column number to ' + drop_or_pop + ': '))
            boards = shared.yellow_pop(user_board, program_board, column)

        else:
            raise game.InvalidMoveError

        if boards != None:
            return red(boards[0], boards[1])
    except ValueError:
        print('\nPlease try again:')
        yellow(ui_board, program_board)
        
    except game.InvalidMoveError:
        print('\nPlease try again:')
        yellow(ui_board, program_board)
        
    except game.GameOverError:
        pass



'''Take input from player Red to either pop or drop a game piece of their own color
    into column of choice'''

def red(user_board, program_board):
    ui_board = user_board
    board_game = program_board
    
    try:
        drop_or_pop = input('\nRED:\nWould you like to "pop" or "drop": ')
        if drop_or_pop.lower() == 'drop':
            column = int(input('\nRED:\nEnter a column number to ' + drop_or_pop + ': '))
            boards = shared.red_drop(user_board, program_board, column)
            
        elif drop_or_pop.lower() == 'pop':
            column = int(input('\nRED:\nEnter a column number to ' + drop_or_pop + ': '))
            boards = shared.red_pop(user_board, program_board, column)

        else:
            raise game.InvalidMoveError

        if boards != None:
            return yellow(boards[0], boards[1])
        
    except ValueError:
        print('\nPlease try again:')
        red(ui_board, program_board)
        
    except game.InvalidMoveError:
        print('\nPlease try again:')
        red(ui_board, program_board)
        
    except game.GameOverError:
        pass


if __name__ == '__main__':

    shared.board_display()
    first()


