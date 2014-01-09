import os.path

def pardir(abspath):
    '''
    get parent dirent of abspath [ either a file or dirent ]
    '''
    if not os.path.isdir(abspath):
        curdir = os.path.dirname(abspath)
    else:
        curdir = abspath
    return os.path.dirname(curdir)

    
    
