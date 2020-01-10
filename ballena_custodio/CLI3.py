import libreria


def opcionA():
     a=libreria.pedir_lista("habitacionesmatrimoniales.txt")
     print("gracias por su preferencia bienvenido a HABITACIONES MATRIMONIALES:", a)

def opcionB():
    b= libreria.pedir_lista("habitacionesnormal.txt")
    print("gracias por su preferencia bienvenido a HABITACIONES NORMALES:", b)


def opcionC():
    c= libreria.pedir_lista("habitacionessimples.txt")
    print("gracias por su preferencia bienvenido a HABITACIONES SIMPLESM L,.-:",c)


opc=0
max=4
while(opc!=max):
    # 1. IMPRESION DEL MENU
    print("########## SERVICIOS DE HOTEL EL PARAISO SOÑADO ########")
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

