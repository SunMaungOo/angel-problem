from .config import EMPTY_SPACE
from .config import BLOCK_SPACE
from .config import ANGLE_SPACE
from .util import check_valid_index

class Board:
    
    def __init__(self,width:int,height:int):
        if width<=0:
            raise Exception("Width must be positive")
        
        if height<=0:
            raise Exception("Height must be positive")
        
        self.__board = list()
        
        for i in range(height):
            row = list()
            
            for j in range(width):
                row.append(EMPTY_SPACE)
            
            self.__board.append(row)
            
        self.__size = (width,height)
        
    def get_size(self,)->tuple:
        """
        Get the (width,height) of the board
        """
        return self.__size
    
    def fill(self,row_index:int,column_index:int,value:str):
        """
        Fill the position with a value
        """
        
        check_valid_index(row_index,"Invalid row index")
        
        check_valid_index(column_index,"Invalid column index")
        
        self.__board[row_index][column_index]=value
        
    def is_filled(self)->bool:
        """
        Check whether all the position is filled in the board
        """
        for row in self.__board:
            for column in row:
                if column==EMPTY_SPACE:
                    return False
                
        return True
    
    def get_position(self,row_index:int,column_index:int)->str:
        """
        Get the value at the position
        """
        
        check_valid_index(row_index,"Invalid row index")

        check_valid_index(column_index,"Invalid column index")
  
        return self.__board[row_index][column_index]
    
    def is_blocked(self,row_index:int,column_index:int)->bool:
        """
        Return whether the position is blocked
        """ 
        return self.get_position(row_index,column_index)==BLOCK_SPACE
    
    def get_avaliable_position(self)->set:
        """
        Return set of position (tuple of row index column index)
        which is empty
        """
        
        avaliable_position = set()
        
        board_size =  self.get_size()
        
        for i in range(board_size[1]):
            for j in range(board_size[0]):
                if self.is_blocked(i,j):
                    continue
                avaliable_position.add((i,j))
            
        return avaliable_position
    
    def remove_angel(self):
        """
        Remove the move angel have made
        """
        for row in self.__board:
            for column_index in range(len(row)):
                column = row[column_index]
                if column==ANGLE_SPACE:
                    row[column_index]=EMPTY_SPACE     
                    return
    
    def pretty_print(self):
        print('\n'.join(['|'.join([str(cell) for cell in row]) for row in self.__board]))
    
                
        
    