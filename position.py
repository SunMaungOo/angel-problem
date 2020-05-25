class Position:
    def __init__(self,
                 row_index:int,
                 column_index:int,
                 rect):
            
        """
        rect : pygame.Rect
        """
        
        self.row_index = row_index
        
        self.column_index = column_index
        
        self.rect = rect