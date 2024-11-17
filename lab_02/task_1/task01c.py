def task1c(words):
    '''
    words -> lista string-uri
    return -> lista string-uri

    Salvati cuvintele care sunt palindrom in "palindromes"
    '''

    palindromes = []

    ################### TO DO #########################

    check = lambda x : x == x[::-1]
    palindromes = list(filter(check, words))

    ###################################################

    # Nu modificati valoarea de retur a functiei
    return list(palindromes)
