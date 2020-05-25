from .board import Board
from .util import check_valid_index

class Character:
        
    def __init__(self,
                 row_index:int,
                 column_index:int):
        
        self.move(row_index,column_index)
    
    def move(self,row_index:int,column_index:int):
        """
        Move the character to the position
        """
        
        check_valid_index(row_index,"Invalid character row index")
        
        check_valid_index(column_index,"Invalid character column index")
        
        self.__position=(row_index,column_index)
            
    def get_position(self)->tuple:
        """
        Return tuple(row_index,column_index) which 
        represent the current position of the character
        """
        return self.__position
    
    def get_avaliable_move(self,board:Board)->set:
        """
        Return set of tuple(row_index,column_index) which
        character can move based on the board
        board : Board to consider
        """
        pass