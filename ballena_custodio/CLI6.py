import libreria


def opcionA():
     a=libreria.pedir_lista("mana.txt")
     print("gracias por escuchar radio oxigeno, cual de sus canciones de mana le gusta", a)

def opcionB():
    b= libreria.pedir_lista("enanitosverdes.txt")
    print("gracias por escuchar radio oxigeno, cual de sus canciones de enanitosverdes le gusta", b)


def opcionC():
    c= libreria.pedir_lista("pedrosuarezvertiz.txt")
    print("gracias por escuchar radio oxigeno, cual de sus canciones de pedrosuarezvertiz le gusta",c)


opc=0
max=4
while(opc!=max):
    # 1. IMPRESION DEL MENU
    print("########## RANKING DE ARTISTAS NOMINADOS A CANCION  DEL AÑO  ########")
    print("1. opcion A")
    print("2. opcion B")
    print("3. opcion C")
    print("4. SALIR")
    print("######################")
    # 2. ELECCION DE LA OPCION  DEL MENU
    opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

    # 3. MAPEO DE LAS OPCIONES
    if (opc == 1):
        opcionA()
    if (opc == 2):
        opcionB()
    if (opc == 3):
        opcionC()

