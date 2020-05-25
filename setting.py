import io

class Setting:
    def __init__(self,file_location:str):
        self.__file_location = file_location
        self.__config = dict()
            
        with open(file_location,mode='r') as file:
            lines = file.readlines()
            
            for line in lines:
                blocks = line.split("=")
                if len(blocks)>1:
                    key = blocks[0].strip()
                    values = blocks[1].strip()
                    
                    if key=="resolution" or key=="grid":
                        tuple_split = values.split(",")
                        if len(tuple_split)==2:
                            value1 = int(tuple_split[0])
                            value2 = int(tuple_split[1])
                            
                            self.__config[key]=tuple([value1,value2])
                    else:
                        self.__config[key]=int(values)
                                
        

    def get_screen_resolution(self)->tuple:
        """
        Return (width,height) screen size or default tuple
        """
        
        if "resolution" in self.__config:
            return self.__config["resolution"]
       
        return (800,600)
    
    def get_grid(self)->tuple:
        """
        Return (width,height) or default tuple
        """
        
        if "grid" in self.__config:
            return self.__config["grid"]
        
        return (3,2)
    
    def get_n(self)->int:
        """
        Return n or default n value
        """
        
        if "n" in self.__config:
            return self.__config["n"]
        
        return 2
            
        