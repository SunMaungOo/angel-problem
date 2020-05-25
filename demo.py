from core import Board
from core import Angel
from core import Devil
from core import ANGLE_SPACE
from core import BLOCK_SPACE
from core import is_terminal
from core import create_character


import random


def start(width:int,height:int,n:int):
    """
    Start the game
    width : Width of the board
    height : Height of the board
    n : How many move the angel wanted to consider from current position
    """
    
    board = Board(width,height)
    
    (angel,devil) = create_character(board,n)
    
    turn = 0 
    
    while not is_terminal(board,angel):
        
        turn+=1
        
        angel_position = angel.get_position()
        
        devil_position = devil.get_position()
        
        #Initial random angel move
        
        board.fill(angel_position[0],angel_position[1],ANGLE_SPACE)
        
        #Initial random devil move
        
        board.fill(devil_position[0],devil_position[1],BLOCK_SPACE)

        print("Current board")
        
        board.pretty_print()
        
        print("******************")
        
        #Angel turn
        
        print("Angle turn") 
         
        board,angel_choosen_move = angel_move(board,angel)
        
        print("Current board")
        
        board.pretty_print()
        
        print("******************")

        #Devil turn

        print("Devil turn")
        
        board = devil_move(board,angel_choosen_move,devil)
                        
    print(f"Game end at turn:{turn}")

def angel_move(board:Board,angel:Angel):
    """
    (new_board,angel choosen move)
    """
    
    angel_avaliable_move = angel.get_avaliable_move(board)
    
    #Input as 3,4   [which are row index]
    
    angel_choosen_move = None
    
    while angel_choosen_move not in angel_avaliable_move:    
        print("As an angel, you can move to")
        print(angel_avaliable_move)
        
        angel_choosen_move = tuple(int(x.strip()) for x in input().split(','))

    #Remove previous move angel have make
        
    board.remove_angel()
    
    board.fill(angel_choosen_move[0],angel_choosen_move[1],ANGLE_SPACE)
        
    angel.move(angel_choosen_move[0],angel_choosen_move[1])
    
    return board,angel_choosen_move

def devil_move(board:Board,angel_choosen_move:tuple,devil:Devil):
    """
    Return new board
    """
    
    devil.set_angel_position(angel_choosen_move)
                
    devil_avaliable_move = devil.get_avaliable_move(board)
    
    devil_choosen_move = None
    
    while devil_choosen_move not in devil_avaliable_move:   
        print("As an devil, you can move to")
        print(devil_avaliable_move)   
        
        devil_choosen_move = tuple(int(x.strip()) for x in input().split(','))
         
    board.fill(devil_choosen_move[0],devil_choosen_move[1],BLOCK_SPACE)
    
    return board

if __name__ == "__main__":
    start(5,3,2)