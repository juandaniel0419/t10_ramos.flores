import libreria


def opcionA():
     a=libreria.pedir_lista("operacionesbancariaspasivas.txt")
     print("que tipo de operacion bancaria desea realizar ", a)

def opcionB():
    b= libreria.pedir_lista("operacionesbancariasactivas.txt")
    print("que tipo de operacion bancaria desea realizar", b)


def opcionC():
    c= libreria.pedir_lista("tiposdecheques.txt")
    print("que tipo de operacion bancaria desea realizar",c)


opc=0
max=4
while(opc!=max):
    # 1. IMPRESION DEL MENU
    print("########## BANCO DE LA NACION ########")
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
