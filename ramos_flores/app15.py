import libreria
# MENU DE UTILES
# EL MENU MOSTRARA 4 OPCCIONES QUE DEBERAN ELEGIR CON LOS NUMEROS(1-4)
def pedir_faber():
    n = libreria.pedir_nombre("ingrese nombre de comprador:")
    c = libreria.pedir_numero("ingrese la cantidad de mochilas que desea comprar:", 1, 100)
    print("el cliente", n, "compro", c, "lapiceros faber castell")

def pedir_pilot():
    n = libreria.pedir_nombre("ingrese nombre de comprador:")
    c = libreria.pedir_numero("ingrese la cantidad de mochilas que desea comprar:", 1, 100)
    print("el cliente", n, "compro", c, "lapiceros pilot")
def pedir_artesco():
    n = libreria.pedir_nombre("ingrese nombre de comprador:")
    c = libreria.pedir_numero("ingrese la cantidad de mochilas que desea comprar:", 1, 100)
    print("el cliente", n, "compro", c, "lapiceros artesco")

def pedir_porta():
    n = libreria.pedir_nombre("ingrese nombre de comprador:")
    c = libreria.pedir_numero("ingrese la cantidad de mochilas que desea comprar:", 1, 100)
    print("el cliente", n, "compro", c, "mochilas porta")
def pedir_adidas():
    n = libreria.pedir_nombre("ingrese nombre de comprador:")
    c = libreria.pedir_numero("ingrese la cantidad de mochilas que desea comprar:", 1, 100)
    print("el cliente", n, "compro", c, "mochilas adidas")


def pedir_caterpilar():
    n = libreria.pedir_nombre("ingrese nombre de comprador:")
    c = libreria.pedir_numero("ingrese la cantidad de mochilas que desea comprar:", 1, 100)
    print("el cliente", n, "compro", c, "mochilas caterpilar")
def pedir_loro():
    n=libreria.pedir_nombre("ingrese nombre de comprador:")
    c=libreria.pedir_numero("ingrese la cantidad de cuadennos que desea comprar:",1,100)
    print("el cliente",n,"compro",c,"cuadernos loro")
def pedir_stanford():
    n = libreria.pedir_nombre("ingrese nombre de comprador:")
    c = libreria.pedir_numero("ingrese la cantidad de cuadennos que desea comprar:", 1, 100)
    print("el cliente", n, "compro", c, "cuadernos stanford")
def pedir_alpha():
    n = libreria.pedir_nombre("ingrese nombre de comprador:")
    c = libreria.pedir_numero("ingrese la cantidad de cuadennos que desea comprar:", 1, 100)
    print("el cliente", n, "compro", c, "cuadernos alpha")

def pedir_cuadernos():
    opc=0
    max=4
    while(opc!=max):
        print("#### cuadernos ####")
        print("# 1 loro")
        print("# 2 stanford")
        print("# 3 alpha")
        print("# 4 salir")
        opc=libreria.pedir_numero("ingrese opcion:",1,4)

        if(opc==1):
            pedir_loro()
        if(opc==2):
            pedir_stanford()
        if(opc==3):
            pedir_alpha()


def pedir_mochila():
    opc = 0
    max = 4
    while (opc != max):
        print("#### mochilas ####")
        print("# 1 porta")
        print("# 2 adidas")
        print("# 3 caterpilar")
        print("# 4 salir")
        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

        if (opc == 1):
            pedir_porta()
        if (opc == 2):
            pedir_adidas()
        if (opc == 3):
            pedir_caterpilar()

def pedir_lapiceros():
    opc = 0
    max = 4
    while (opc != max):
        print("#### lapiceros ####")
        print("# 1 faber castell")
        print("# 2 pilot")
        print("# 3 artesco")
        print("# 4 salir")
        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

        if (opc == 1):
            pedir_faber()
        if (opc == 2):
            pedir_pilot()
        if (opc == 3):
            pedir_artesco()


opc=0
max=4
# MENU GENERAL
while(opc!=max):
    print("####### UTILES #######")
    print("1.-Cuadernos")
    print("2.-Mochilas")
    print("3.-Lapiceros")
    print("4.-Salir")
    # ELECCION DE LA OPCION DEL MENU
    opc = libreria.pedir_numero("Ingrese la opcion que desea comprar:", 1, 4)
    if(opc==1):
        pedir_cuadernos()
    if(opc==2):
        pedir_mochila()
    if(opc==3):
        pedir_lapiceros()
print("FIN DEL MENU")
# FIN DEL MENU

