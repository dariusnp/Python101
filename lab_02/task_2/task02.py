def task(*args):
    '''
    args -> elemente de tipuri diferite
    return -> lista cu elementele corespunzatoare
    '''

    result = []
    voc = 'aeiouAEIOU'
    ################### TO DO #########################
    
    for var in args:
        if (type(var) == int):
            result.append(var)
        elif(type(var) == str and len(var) < 4):
            if(var not in voc and ord(var) > 96 and ord(var) < 123):
                result.append(var)


    ###################################################
    
    return result
