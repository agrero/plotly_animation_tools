# there is alikely a way to name axis so this isn't a necessity
def create_typename(names:list, name:str):
    # check if name is alread in
    # both name and number are in the list already
    if name in names and any(char.isdigit() for char in name):
        name = [i for i in name] # make malleable
        name[-1] = int(name[-1]) + 1 # add one

        create_typename(names, ''.join(name)) # recursively call 
    
    # if its the first repeat
    elif name in names: 
        name = f'{name}2' # idk why its 2
        return name
    
    # it is the first instance
    else:
        return name