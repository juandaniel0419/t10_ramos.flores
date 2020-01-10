import libreria


def opcionA():
     a=libreria.pedir_lista("ingresos.txt")
     print("que tipo  de informacion desea saber sobre los INGRESOS del presupuesto general ", a)

def opcionB():
    b= libreria.pedir_lista("egresos.txt")
    print("que tipo  de informacion desea saber sobre los EGRESOS del presupuesto general", b)


opc=0
max=3
while(opc!=max):
    # 1. IMPRESION DEL MENU
    print("########## PRESUPUESTO GENERAL DE LA REPUBLICA DEL PERU ########")
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
