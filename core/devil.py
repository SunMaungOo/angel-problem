from .character import Character
from .board import Board

class Devil(Character):
    def __init__(self,
                 row_index:int,
                 column_index:int,
                 angel_position:tuple):
        
        Character.__init__(self,row_index,column_index)
        
        self.set_angel_position(angel_position)
            
    def set_angel_position(self,angel_position:tuple):
        
        self.__angel_position = angel_position 
    
    def __get_angel_position(self):
        return self.__angel_position
                
    def get_avaliable_move(self,
                           board:Board)->set:
        
        
        devil_avaliable_move = board.get_avaliable_position()
        
        #We need to remove angel position from devil avaliable position  
         
        devil_avaliable_move.remove(self.__get_angel_position())
                
        return devil_avaliable_move