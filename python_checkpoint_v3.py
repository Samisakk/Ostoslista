import operator
lista = []
tuple = ()
while True: 
    print("")
    print("1. Lisää tuote: ")
    print("2. Listalla olevat tuotteet: ")
    print("3. Kallein tuote: ")
    print("4. Halvin hinta: ")
    print("5. Tyhjennä lista")
    print("6. Lopetus")
    
    valinta = input("Mitä haluat tehdä? >")
    if valinta == "1":
        try:
            while True:
                tuote = input("Anna tuote: [x lopettaa]: > ")
                if tuote == "x":
                    break
                hinta = input("Anna hinta: >") 
                tuple = (hinta, tuote)
                lista.append(tuple)
        except AttributeError:
                print("Lisäämisessä tapahtui virhe, yritä uudelleen.")
    elif valinta == "2":
        try:
            print("Listalla olevat tuotteesi:")
            print("----------------------------------------")
            for x in lista:
                print(x)
                print("----------------------------------------")
            if len(lista)==0:
                print("Lista on tyhjä")    
        except TypeError:
            print("Lista on tyhjä")
    elif valinta == "3":
        if len(lista)== 0:
            print("----------------------------------------")  
            print("lisää ensin tuote tuote jotta voit laskea kalleimman: ")
            print("----------------------------------------") 
        else:    
            print("----------------------------------------")        
            print(f"Kallein hinta on: {max(lista, key=operator.itemgetter(0))}")
            print("----------------------------------------")  
    elif valinta == "4":
        if len(lista) == 0:
            print("----------------------------------------")  
            print("lisää ensin tuote tuote jotta voit laskea halvimman: ")
            print("----------------------------------------")  
        else:
            print("----------------------------------------")  
            print(f"Halvin hinta on: {min(lista, key=operator.itemgetter(0))}")
            print("----------------------------------------")  
    elif valinta == "5":
        if len(lista) == 0:
            print("Lista on tyhjä")
        else: 
            lista= [] 

    elif valinta == "6":
        print("########################################")  
        print("#-----------------LOPPU----------------#")  
        print("########################################")  
        break
