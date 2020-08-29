# we do it iteration because we have limit memory, 
# we cannot run recursive because that take more memory

def search(names, item):
    start = 0
    end = len(names) - 1
    while end > start:
        # start at middle of the list
        guess = (start + end) // 2  #interget division
        if names[guess] == item:
            return True
        elif names[guess] < item:
            start = guess + 1
        else:
            end = guess - 1
    return False