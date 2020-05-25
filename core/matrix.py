from .board import Board

def get_avaliable_moves(board:Board,position:tuple,n:int)->set:
    """
    Return all the avaliable move from the position
    Return set will be a set of tuple (row_index,column_index)
    the set will ignore the current position and all the blocked position
    board : 2D matrix (composed on list(list))
    position : Position to get the avaliable position.
               Tuple of row_index , column_index
    n : How many neighbor/move we wanted to consider from the current position
    """
    
    avaliable_move = set()
    
    (row_start_index,
     row_end_index,
     column_start_index,
     column_end_index) =  get_neighbor_bound(board.get_size(),position,n)
    
    board_size = board.get_size()
    
    board_width = board_size[0]
    
    board_height = board_size[1]
    
    #width/column index
    for i in range(row_start_index,row_end_index+1):
        #height/row index
        for j in range(column_start_index,column_end_index+1):
            
            #Need to only take into consideration the valid move
            
            if i<0 or j<0:
                continue
            
            #if it is out of range
            
            if not (i<board_height and j<board_width):
                continue

            move = (i,j)
            
            #If it the current position , we ignore it
            
            if move==position:
                continue
        
            #Ignore if the move is blocked
                        
            if board.is_blocked(i,j):
                continue
            
            avaliable_move.add(move)
            
    return avaliable_move
    

def get_neighbor_bound(size:tuple,position:tuple,n:int)->tuple:
      
    """
    Get the bound of the neighbour
    size : (width,height) tuple of the board
    position : (row_index,column_index) to get bound of
    return (row_start_index,row_end_index,
    column_start_index,column_end_index)
    """
        
    cell_row_index = position[0]
        
    cell_column_index = position[1]
        
    width_index = size[0]-1
        
    height_index = size[1]-1
        
    top_left = (cell_row_index==0 and cell_column_index==0)
        
    top_right = (cell_row_index==0 and cell_column_index==height_index)
        
    bottom_left = (cell_row_index==width_index and cell_column_index==0)
        
    bottom_right = (cell_row_index==width_index and cell_column_index==height_index)
   
    row_start_index = -1
        
    row_end_index = -1
        
    column_start_index=-1
        
    column_end_index = -1
        
    if top_left:
        row_start_index=0
        row_end_index=n
        column_start_index=0
        column_end_index=n
            
    elif top_right:
        row_start_index=0
        row_end_index=n
        column_start_index=width_index-n
        column_end_index=width_index
            
    elif bottom_left:
        row_start_index=height_index-n
        row_end_index=height_index
        column_start_index=0
        column_end_index=n
            
    elif bottom_right:
        row_start_index=height_index-n
        row_end_index=height_index
        column_start_index=width_index-n
        column_end_index=width_index
            
    else:
        row_start_index=cell_row_index-n
        row_end_index=cell_row_index+n
        column_start_index=cell_column_index-n
        column_end_index=cell_column_index+n

    return (row_start_index,
            row_end_index,
            column_start_index,
            column_end_index)
    
    