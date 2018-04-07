print('Imported my_module...')

test = 'Test string'

def find_index(to_search, target):
    ''' find the index of the value in the sequence'''
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1
