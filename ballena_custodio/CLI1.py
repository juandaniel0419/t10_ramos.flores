import libreria
#

def opcionA():
     a=libreria.pedir_lista("facfym.txt")
     print("mostrar las escuelas de facfym", a)

def opcionB():
    b= libreria.pedir_lista("fiquia.txt")
    print("Ud. se incribio  a la facultad de FIQUIA", b)


def opcionC():
    c= libreria.pedir_lista("fachse.txt")
    print("Ud. se inscribio a la facultad de FACHSE",c)


opc=0
max=4
while(opc!=max):
    # 1. IMPRESION DEL MENU
    print("########## FACULTAD  ########")
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

