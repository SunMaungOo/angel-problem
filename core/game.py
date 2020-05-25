from .board import Board
from .angel import Angel
from .devil import Devil

import random

def is_terminal(board:Board,angel:Angel):
    """
    Game end when all the position of the board is full
    or angel cannot run based on it current position
    """
        
    return board.is_filled() or len(angel.get_avaliable_move(board))==0

def create_character(board:Board,n:int):
    """
    Return (angel,devil) tuple with their position
    in random 
    """
 
    board_avaliable_position = board.get_avaliable_position()
        
    (angel_row_index,angel_column_index) = random.choice(list(board_avaliable_position))
    
    angel = Angel(angel_row_index,angel_column_index,n)
    
    #Remove angel position
    
    board_avaliable_position.remove((angel_row_index,angel_column_index))
    
    (devil_row_index,devil_column_index) = random.choice(list(board_avaliable_position))

    devil = Devil(devil_row_index,devil_column_index,angel.get_position())
    
    return (angel,devil)