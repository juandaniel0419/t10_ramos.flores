import libreria
def mostrar_i():

    datos = libreria.obtener_datos("ing.txt")
    if (datos != ""):
        print(datos)
    else:
        print("archivos sin datos")

def mostrar_e():
    datos = libreria.obtener_datos("emp.txt")
    if (datos != ""):
        print(datos)
    else:
        print("archivos sin datos")


def mostrar_n():
    datos = libreria.obtener_datos("uni.txt")
    if (datos != ""):
        print(datos)
    else:
        print("archivos sin datos")


def mostrar_p():
    datos = libreria.obtener_datos("par.txt")
    if (datos != ""):
        print(datos)
    else:
        print("archivos sin datos")

def mostrar_c():
    opc = 0
    max = 3
    while (opc != max):
        print("#### mostrar carreras####")
        print("# 1. ingenierias")
        print("# 2. empresariales")
        print("# 3. salir")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 3)
        if(opc==1):
            mostrar_i()
        if(opc==2):
            mostrar_e()





def mostrar_u():
    opc = 0
    max = 3
    while (opc != max):
        print("#### mostrar universidades ####")
        print("# 1. universidades nacionales")
        print("# 2. universidades particulares")
        print("# 3. salir")

        opc = libreria.pedir_numero("ingrese opcion:", 1, 3)
        if (opc == 1):
            mostrar_n()
        if (opc == 2):
            mostrar_p()
opc=0
max=3
while(opc!=max):
    print("#### menu ####")
    print("# 1. mostrar carreras profesionales")
    print("# 2. mostrar universidades")
    print("# 3. salir")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        mostrar_c()
    if(opc==2):
        mostrar_u()

print("find del programa")
