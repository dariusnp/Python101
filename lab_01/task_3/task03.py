def func(string_message):
    """ 
    Puneti rezultatul codificarii mesajului in "encoded_message"

    HINT!
    chr() si ord() sunt functii implicite care "jongleaza" cu caracterele
    ASCII si codificarile lor. Astfel, daca pentru litera 'A', avem codificarea
    65, iar pentru 'B' avem 66, atunci:
    
    chr(65) = 'A'   ||   chr(66) = 'B'  
    ord('A') = 65   ||   ord('B') = 66

    ANOTHER HINT!
    Poti folosi dictionarele.
    """
    
    encoded_message = ""
    dictionary = {" " : 0}
    ################### TO DO #########################

    for i in range(65, 90):
        dictionary[chr(i)] = ord(chr(i)) - 64

    for litera in string_message:
        a = str(dictionary[litera])
        encoded_message += a

    ###################################################

    return encoded_message