import libreria


def Elegir_oyemiamor():
    a=libreria.pedir_lista("mana.txt")
    print(a)
    print(a[0])

def Elegir_tellevarealcielo():
    b = libreria.pedir_lista("mana.txt")
    print(b)
    print(b[0])

def Elegir_clavadoenunbar():
    c = libreria.pedir_lista("mana.txt")
    print(c)
    print(c[0])

def Mostrar_MANA():
    opc = 0
    max = 4
    while (opc != max):
        # 1. IMPRESION DEL MENU
        print("########## MANA  ########")
        print("1. OYE MI AMOR")
        print("2. TE LLEVARE AL CIELO")
        print("3. CLAVADO EN UN BAR")
        print("######################")
        # 2. ELECCION DE LA OPCION  DEL MENU
        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

        # 3. MAPEO DE LAS OPCIONES
        if (opc == 1):
             Elegir_oyemiamor()
        if (opc == 2):
            Elegir_tellevarealcielo()
        if (opc == 3):
            Elegir_clavadoenunbar()


def Elegir_cuandopiensesenvolver():
    d=libreria.pedir_lista("pedrosuarezvertiz.txt")
    print(d)
    print(d[0])

def Elegir_losglobosdelcielo():
    e = libreria.pedir_lista("pedrosuarezvertiz.txt")
    print(e)
    print(e[0])

def Elegir_tesientodesolopensar():
    f = libreria.pedir_lista("pedrosuarezvertiz.txt")
    print(f)
    print(f[0])

def Mostrar_PEDROSUAREZVERTIZ():
    opc = 0
    max = 4
    while (opc != max):
        # 1. IMPRESION DEL MENU
        print("########## PEDRO SUAREZ VERTIZ  ########")
        print("1. CUANDO PIENSES EN VOLVER")
        print("2. LOS GLOBOS DEL CIELO")
        print("3. TE SIENTO DE SOLO PENSAR")
        print("######################")
        # 2. ELECCION DE LA OPCION  DEL MENU
        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

        # 3. MAPEO DE LAS OPCIONES
        if (opc == 1):
             Elegir_cuandopiensesenvolver()
        if (opc == 2):
            Elegir_losglobosdelcielo()
        if (opc == 3):
            Elegir_tesientodesolopensar()




def Elegir_lamurallaverde():
    g=libreria.pedir_lista("enanitosverdes.txt")
    print(g)
    print(g[0])

def Elegir_yotevi():
    h = libreria.pedir_lista("enanitosverdes.txt")
    print(h)
    print(h[0])

def Elegir_tucarcel():
    i = libreria.pedir_lista("enanitosverdes.txt")
    print(i)
    print(i[0])

def Mostrar_ENANITOSVERDES():
    opc = 0
    max = 4
    while (opc != max):
        # 1. IMPRESION DEL MENU
        print("########## ENANITOS VERDES  ########")
        print("1. LA MURALLA VERDE ")
        print("2. YO TE VI")
        print("3. TU CARCEL")
        print("4. SALIR")
        print("######################")
        # 2. ELECCION DE LA OPCION  DEL MENU
        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

        # 3. MAPEO DE LAS OPCIONES
        if (opc == 1):
            Elegir_lamurallaverde()
        if (opc == 2):
            Elegir_yotevi()
        if (opc == 3):
            Elegir_tucarcel()


opc = 0
max = 4
while(opc!=max):
    # 1. IMPRESION DEL MENU
    print("########## RANKING DE ARTISTAS NOMINADOS A CANCION  DEL AÑO  ########")
    print("1. MANA")
    print("2. PEDRO SUAREZ VERTIZ")
    print("3. ENANITOS VERDES")
    print("4. SALIR")
    print("######################")
    # 2. ELECCION DE LA OPCION  DEL MENU
    opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

    # 3. MAPEO DE LAS OPCIONES
    if (opc == 1):
        Mostrar_MANA()
    if (opc == 2):
        Mostrar_PEDROSUAREZVERTIZ()
    if (opc == 3):
        Mostrar_ENANITOSVERDES()
