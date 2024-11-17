def task1a(nums):
    '''
    nums -> vector int
    return -> vector int

    Dublati elementele care se divid cu 6, iar pe cele 
    care nu se divid, triplati-le folosind functionale
    '''

    result = []

    ################### TO DO #########################

    trip = lambda x : x * 3
    dub = lambda x : x * 2
    div_six = lambda x : x % 6 == 0

    test = lambda x : dub(x) if(div_six(x)) else trip(x)

    result = map(test, nums)

    ###################################################

    # Nu modificati valoarea de retur a functiei
    return list(result)
