import sys, pygame

from core import Board
from core import BLOCK_SPACE
from core import ANGLE_SPACE

from color import BLACK
from color import GREEN
from color import BLUE
from color import RED
from color import WHITE

from gamelogic import GameLogic
from position import Position
from setting import Setting

import os

def get_cell_size(screen_width:int,
                  screen_heigth:int,
                  board_size:tuple)->tuple:
    """
    Return (width,height) of individual cell
    """    
    cell_width = (screen_width/board_size[0])
    
    cell_height = (screen_heigth/board_size[1])
    
    cell_size = (int(cell_width),int(cell_height))
    
    return cell_size


def get_rect(width:int,
             height:int,
             cell_size:tuple)->pygame.Rect:
    
    return pygame.Rect(height*cell_size[0],
                       width*cell_size[1],
                       cell_size[0],
                       cell_size[1])

def get_font(font_location:str):
    """
    Tuple of pygame.font
    Return (small_font,medium_font,large_font)
    """
    
    small_font = pygame.font.Font(font_location,20)
    
    medium_font = pygame.font.Font(font_location,28)
    
    large_font = pygame.font.Font(font_location,40)
    
    return (small_font,medium_font,large_font)

def center(screen_width:int,
           texts:list,
           font:pygame.font)->list:
    """
    Return list of tuple(surface,center_rect)
    
    screen_width:Width of the screen
    texts:text we wanted to center.Each item of text will be separted by 
    new line
    font:pygame font we wanted to use
    """
    
    center_texts = list()
    
    for i,text in enumerate(texts):   
        line = font.render(text,True,WHITE)
        rect = line.get_rect()
        rect.center = ((screen.get_width() / 2), (150 + 30*i))
        screen.blit(line, rect)
        center_texts.append((line,rect))
        
    return center_texts

def show_game_over_screen(screen:pygame.Surface,
                          font:pygame.font,
                          game_logic:GameLogic)->bool:
    """
    Show game over
    """
    
    game_turn = "Turn : "+ str(game_logic.get_turn_count())
            
    for line,rect in center(screen.get_width(),["Game Over",
                                                game_turn,
                                                "Press enter to exit"],font):
        screen.blit(line,rect)
    

def show_playing_screen(screen:pygame.Surface,
                        cell_size:tuple,
                        angel_icon,
                        devil_icon,
                        game_logic:GameLogic):
    """
    Show the playing screen
    Return (new game logic which is changed,whether a move is made)
    """
    
    move_made = False
    
    board_size = game_logic.get_board().get_size()

    board_width = board_size[0]
    
    board_height = board_size[1]
    #width/column index
    for column_index in range(board_width):
        #height/row index
        for row_index in range(board_height):
                 
            if not (column_index<board_width and row_index<board_height):
                continue
                    
            rect = get_rect(row_index,column_index,cell_size)
                    
            #If the position is angel position
            
            if game_logic.get_board().get_position(row_index,column_index)==ANGLE_SPACE:
                screen.blit(angel_icon,rect)
            
            #If the position is devil position
                                        
            elif game_logic.get_board().get_position(row_index,column_index)==BLOCK_SPACE:
                screen.blit(devil_icon,rect)
            else:
                pygame.draw.rect(screen,BLACK,rect)
                    
            positions = list()
            
            is_angel_turn = game_logic.is_angel_turn()
            
            avaliable_moves = set()
            
            if is_angel_turn:
                avaliable_moves = game_logic.get_avaliable_angel_moves()
            else:
                avaliable_moves = game_logic.get_avaliable_devil_moves()
            
            for (i,j) in avaliable_moves:
                
                rect = get_rect(i,j,cell_size)
                    
                pygame.draw.rect(screen,BLUE,rect)
                    
                positions.append(Position(i,j,rect))
                      
            left_clicked,_,_ = pygame.mouse.get_pressed()
            
            #if left clicked
            if left_clicked==1:
                
                mouse = pygame.mouse.get_pos()
                
                for position in positions:
                    #if the avaliable position is clicked
                    if position.rect.collidepoint(mouse):
                        
                        move_made = True
                        
                        #if it is an angel turn,move the angel
                        if is_angel_turn:                        
                            game_logic.angel_move(position.row_index,
                                                position.column_index)
                        else:
                            game_logic.devil_move(position.row_index,
                                                position.column_index)
                            
    return game_logic,move_made
   

def show_instruction_screen(screen:pygame.Surface,
                            font:pygame.font,
                            game_logic:GameLogic):
    
    lines = list()
    
    if game_logic.is_angel_turn():
        lines.append("You are an angel")
        lines.append("You need to get away from devil")
        lines.append(f"You can move {game_logic.get_angel_n()} from current position")
        lines.append("Click on any blue square to run away")
    else:
        lines.append("You are a devil")
        lines.append("You need to catch an angel")
        lines.append("Click on any blue square to trap an angel")
    
    lines.append("Press enter to get play the game")
    lines.append("If you don't want to see instruction again,Press i")
    
    for line,rect in center(screen.get_width(),lines,font):
        screen.blit(line,rect)
    
    
def game_loop(screen:pygame.Surface,
              cell_size:tuple,
              game_logic:GameLogic):
    """
    cell_size : Invidiual cell size (cell_width,cell_height)
    """
    
    small_font,medium_font,large_font = get_font(resource_path("assets/fonts/OpenSans-Regular.ttf"))
  
    angel_icon = pygame.image.load(resource_path("assets/images/angel.png")).convert()
    angel_icon = pygame.transform.scale(angel_icon,cell_size)
    
    devil_icon = pygame.image.load(resource_path("assets/images/devil.jpg")).convert()
    devil_icon = pygame.transform.scale(devil_icon,cell_size)
    
    
    is_instruction = True
    
    is_ignore_instruction = False
    
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        screen.fill(BLACK)   
        
        if game_logic.is_game_over():
                     
            show_game_over_screen(screen,
                                  medium_font,
                                  game_logic)
            
            if event.type==pygame.KEYDOWN and event.key==pygame.K_RETURN:
                break   
                 
        elif is_instruction and not is_ignore_instruction:
                        
            show_instruction_screen(screen,
                                    medium_font,
                                    game_logic)
            
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    is_instruction=False
                elif event.key==pygame.K_i:
                    is_ignore_instruction = True        
        else:
                  
            game_logic,move_made  = show_playing_screen(screen,
                                                        cell_size,
                                                        angel_icon,
                                                        devil_icon,
                                                        game_logic)
            
            is_instruction = move_made
                     
        pygame.display.flip()

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
        
if __name__ == "__main__":
    
    setting = Setting(resource_path("setting.config"))
    
    screen_resolution = setting.get_screen_resolution()
    
    grid = setting.get_grid()
    
    pygame.init()
    
    game_logic = GameLogic(Board(grid[0],grid[1]),setting.get_n())
    game_logic.init()
    
    screen = pygame.display.set_mode(screen_resolution)

    cell_size = get_cell_size(screen_resolution[0],
                              screen_resolution[1],
                              game_logic.get_board().get_size())

    game_loop(screen,cell_size,game_logic)
  
    
    
