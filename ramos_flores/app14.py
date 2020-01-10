import libreria
def mostrar_i():

    datos = libreria.obtener_datos("pai.txt")
    if (datos != ""):
        print(datos)
    else:
        print("archivos sin datos")

def mostrar_e():
    datos = libreria.obtener_datos("lim.txt")
    if (datos != ""):
        print(datos)
    else:
        print("archivos sin datos")


def mostrar_n():
    datos = libreria.obtener_datos("cont.txt")
    if (datos != ""):
        print(datos)
    else:
        print("archivos sin datos")


def mostrar_p():
    datos = libreria.obtener_datos("pote.txt")
    if (datos != ""):
        print(datos)
    else:
        print("archivos sin datos")

def mostrar_c():
    opc = 0
    max = 3
    while (opc != max):
        print("#### mostrar paises sudamericanos####")
        print("# 1. paises que fueron al mundial russia 2018")
        print("# 2. paises que limitan con peru")
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
        print("#### mostrar continentes ####")
        print("# 1. continentes ")
        print("# 2. paises potencia")
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
    print("# 1. mostrar paises de sudamerica")
    print("# 2. mostrar continetes")
    print("# 3. salir")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        mostrar_c()
    if(opc==2):
        mostrar_u()

print("find del programa")
