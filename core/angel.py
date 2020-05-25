from .character import Character
from .board import Board
from .matrix import get_avaliable_moves

class Angel(Character):
    
    def __init__(self,
                 row_index:int,
                 column_index:int,
                 n:int):
        """
        n : how many move the angel wanted to consider from current position
        """
        
        Character.__init__(self,row_index,column_index)
        
        self.__n = n
                   
    def get_avaliable_move(self,
                           board:Board)->set:
        """
        Return set of tuple(row_index,column_index) can move 
        based on the board
        board : Board to consider
        """
        return get_avaliable_moves(board,self.get_position(),self.__n)
        
        