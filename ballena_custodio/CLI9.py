import libreria


def opcionA():
     a=libreria.pedir_lista("universidadeslicenciadas.txt")
     print("estas son las universidades licenciadas por SUNEDU ", a)

def opcionB():
    b= libreria.pedir_lista("universidadesdenegadas.txt")
    print("estos son las universidades denegadas por SUNEDU ", b)


def opcionC():
    c= libreria.pedir_lista("universidadesenprocesodelicenciamiento.txt")
    print("estas universidades estan en observacion por la SUNEDU",c)


opc=0
max=4
while(opc!=max):
    # 1. IMPRESION DEL MENU
    print("########## SUNEDU EN LA REGION LAMBAYEQUE ########")
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
