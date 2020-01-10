import libreria


def Elegir_antonioballenacustodio():
    a=libreria.pedir_lista("faceac.txt")
    print(a)
    print(a[0])

def Elegir_miltoningachiroque():
    b = libreria.pedir_lista("faceac.txt")
    print(b)
    print(b[0])

def Elegir_pepebrenislanegra():
    c = libreria.pedir_lista("faceac.txt")
    print(c)
    print(c[0])

def Mostrar_FACEAC():
    opc = 0
    max = 4
    while (opc != max):
        # 1. IMPRESION DEL MENU
        print("########## FACEAC ########")
        print("1. ANTONIO BALLENA CUSTODIO")
        print("2. MILTON INGA CHIROQUE")
        print("3. PEPE BRENIS LANEGRA")
        print("######################")
        # 2. ELECCION DE LA OPCION  DEL MENU
        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

        # 3. MAPEO DE LAS OPCIONES
        if (opc == 1):
             Elegir_antonioballenacustodio()
        if (opc == 2):
            Elegir_miltoningachiroque()
        if (opc == 3):
            Elegir_pepebrenislanegra()


def Elegir_leonardovivaschayan():
    d=libreria.pedir_lista("fime.txt")
    print(d)
    print(d[0])

def Elegir_yoelsalazarguevara():
    e = libreria.pedir_lista("fime.txt")
    print(e)
    print(e[0])

def Elegir_cinthyavictorianoordoñes():
    f = libreria.pedir_lista("fime.txt")
    print(f)
    print(f[0])

def Mostrar_FIME():
    opc = 0
    max = 4
    while (opc != max):
        # 1. IMPRESION DEL MENU
        print("########## FIME  ########")
        print("1. LEONARDO VIVAS CHAYAN")
        print("2. YOEL SALAZAR GUEVARA")
        print("3. CINTHYA VICTORIANO ORDOÑES")
        print("######################")
        # 2. ELECCION DE LA OPCION  DEL MENU
        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

        # 3. MAPEO DE LAS OPCIONES
        if (opc == 1):
             Elegir_leonardovivaschayan()
        if (opc == 2):
            Elegir_yoelsalazarguevara()
        if (opc == 3):
            Elegir_cinthyavictorianoordoñes()




def Elegir_selenamilianguerrero():
    g=libreria.pedir_lista("fia.txt")
    print(g)
    print(g[0])

def Elegir_sandyfernandezalcantara():
    h = libreria.pedir_lista("fia.txt")
    print(h)
    print(h[0])

def Elegir_emersondiazarrascue():
    i = libreria.pedir_lista("fia.txt")
    print(i)
    print(i[0])

def Mostrar_FIA():
    opc = 0
    max = 4
    while (opc != max):
        # 1. IMPRESION DEL MENU
        print("########## FIA  ########")
        print("1. SELENA MILIAN GUERRERO ")
        print("2. SANDYFERNADEZ ALCANTARA")
        print("3. EMERSON DIAZ ARRASCUE")
        print("4. SALIR")
        print("######################")
        # 2. ELECCION DE LA OPCION  DEL MENU
        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

        # 3. MAPEO DE LAS OPCIONES
        if (opc == 1):
            Elegir_selenamilianguerrero()
        if (opc == 2):
            Elegir_sandyfernandezalcantara()
        if (opc == 3):
            Elegir_emersondiazarrascue()


opc = 0
max = 4
while(opc!=max):
    # 1. IMPRESION DEL MENU
    print("########## ELECCIONES DE DECANOS DE LA UNPRG  ########")
    print("1. FACEAC")
    print("2. FIA")
    print("3. FIME")
    print("4. SALIR")
    print("######################")
    # 2. ELECCION DE LA OPCION  DEL MENU
    opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

    # 3. MAPEO DE LAS OPCIONES
    if (opc == 1):
        Mostrar_FACEAC()
    if (opc == 2):
        Mostrar_FIME()
    if (opc == 3):
        Mostrar_FIA()
