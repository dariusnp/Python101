def task(register):
    '''
    register -> dictionar
    return -> lista doar cu numele studentilor
    '''
    names = []

    ################### TO DO #########################
    
    medie = lambda x : 1 if (sum(x) / len(x) >= 8.50) else 0

    for nume, note in register.items():
        if (medie(note)):
            names.append(nume)

    ###################################################
    
    return names
