def task1b(phrase):
    '''
    phrase -> string
    return -> string

    Transformati in litere mari vocalele din fraza
    si salvati rezultatul in "new_phrase"
    '''

    new_phrase = ""
    voc = 'aeiou'
    ################### TO DO #########################
    
    trans = lambda x : chr(ord(x) - 32)
    check = lambda x : trans(x) if x in voc else x

    new_phrase = map(check, phrase)
    
            
    ###################################################

    # Nu modificati valoarea de retur a functiei
    return ''.join(list(new_phrase))
