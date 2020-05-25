from core import Board
from core import create_character
from core import BLOCK_SPACE
from core import ANGLE_SPACE
from core import is_terminal

class GameLogic:
    def __init__(self,board:Board,n:int):
        self.__board = board
        self.__n = n
        self.__angel_move_count = 0
        self.__devil_move_count = 0
        
    def init(self):
        """
        Init the game logic
        """    
        (angel,devil) = create_character(self.__board,self.__n)

        self.__angel = angel
        
        self.__devil = devil
        
        angel_position = angel.get_position()
            
        devil_position = devil.get_position()    

        #Initial random angel move
            
        self.__board.fill(angel_position[0],angel_position[1],ANGLE_SPACE)

            
        #Initial random devil move
            
        self.__board.fill(devil_position[0],devil_position[1],BLOCK_SPACE)
        
        self.__angel_move_count+=1
        
        self.__devil_move_count+=1
    
    def is_angel_turn(self)->bool:
        """
        Return whether it is an angel turn
        """
        return self.__angel_move_count==self.__devil_move_count
    
    def get_avaliable_angel_moves(self):
        return self.__angel.get_avaliable_move(self.__board)
   
    def get_avaliable_devil_moves(self):
        return self.__devil.get_avaliable_move(self.__board)
 
    def angel_move(self,
                   row_index:int,
                   column_index:int)->bool:
        """
        Whether the angel is actually move
        """
        
        if (row_index,column_index) in self.__angel.get_avaliable_move(self.__board):
            
            self.__angel_move_count+=1
            
            self.__board.remove_angel()
              
            self.__board.fill(row_index,column_index,ANGLE_SPACE)
        
            self.__angel.move(row_index,column_index)
            
            #Update devil track of angel position
            
            self.__devil.set_angel_position(self.__angel.get_position())
            
            return True
        
        return False

    def devil_move(self,row_index:int,column_index:int)->bool:
        """
        Whether the devil is actually move
        """
        if (row_index,column_index) in self.__devil.get_avaliable_move(self.__board):
            
            self.__devil_move_count+=1
            
            self.__board.fill(row_index,column_index,BLOCK_SPACE)
            
            return True
        
        return False

    def get_board(self)->Board:
        """
        Get the board the game logic 
        manage.We should not change 
        anything to the return board
        """
        return self.__board
    
    def is_game_over(self)->bool:
        return is_terminal(self.__board,self.__angel)
    
    def get_turn_count(self)->int:
        """
        Return how many turn it is
        """
        return self.__angel_move_count
        
    def get_angel_n(self)->int:
        return self.__n  