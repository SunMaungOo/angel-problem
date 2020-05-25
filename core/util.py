def check_valid_index(index:int,message:str):
    """
    Check whether the index is valid or throw an 
    exception with a message
    """
    if index<0:
        raise Exception(message)