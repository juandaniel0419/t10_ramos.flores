import libreria


def opcionA():
     a=libreria.pedir_lista("dinastiasHabsburgo.txt")
     print("la dinastia HABSBURGO tuvo a los reyes:", a)

def opcionB():
    b= libreria.pedir_lista("dinastiasBorbonica.txt")
    print("la dinastia BORBONICA tuvo a los reyes: ", b)


opc=0
max=3
while(opc!=max):
    # 1. IMPRESION DEL MENU
    print("########## DINASTIAS DURANTE EL VIRREINATO EN EL PERU ########")
    print("1. opcion A")
    print("2. opcion B")
    print("3. SALIR")
    print("######################")
    # 2. ELECCION DE LA OPCION  DEL MENU
    opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

    # 3. MAPEO DE LAS OPCIONES
    if (opc == 1):
        opcionA()
    if (opc == 2):
        opcionB()

