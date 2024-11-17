def func(nume_complete):
    """
    Creeaza un tuplu "nume_formatat" care sa contina 3 elemente:
    nume_formatat[0] = lista cu numele de familie
    nume_formatat[1] = lista cu primele prenume
    nume_formatat[2] = lista cu celelalte prenume

    HINT!  conversie string - lista || (string.split("delimiter"))
    """


    ################### TO DO #########################

    n = list()
    nume_formatat = ()
    nume_neformatat = list()
    prenume_split = list()
    prenume1 = list()
    prenume2 = list()
    # Iterating through every complete name in the list

    for nume in nume_complete:
        nume_neformatat = nume.split(' ')
        prenume_split = nume_neformatat[1].split('-')

        n.append(nume_neformatat[0])
        prenume1.append(prenume_split[0])
        prenume2.append(prenume_split[1])

    nume_formatat = (n, prenume1, prenume2)
    ###################################################

    return nume_formatat