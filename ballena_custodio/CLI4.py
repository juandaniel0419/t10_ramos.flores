import libreria


def opcionA():
     a=libreria.pedir_lista("apra.txt")
     print("gracias por votar por nuestro partido , no lo defraudaremos", a)

def opcionB():
    b= libreria.pedir_lista("fuerzapopular.txt")
    print("gracias por votar por nuestro partido, no lo defraudaremos", b)


def opcionC():
    c= libreria.pedir_lista("comunista.txt")
    print("gracias por votar por nuestro partido , no lo defraudaremos",c)


opc=0
max=4
while(opc!=max):
    # 1. IMPRESION DEL MENU
    print("########## ELECCIONES DE CONGRESISTAS 2020  ########")
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

