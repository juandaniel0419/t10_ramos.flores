import libreria
# EN ESTE MENU PODRAN ELEGIR VARIAS OPCIONES Y TAMBIEN REALIZAR SU BOLETA DE
# DE CONSUMO
def pedir_lucuma():
    c=libreria.pedir_numero("ingrese numero de helados de lucuma:",1,100)
    print("se ha escogido",c,"helados de lucuma" )
def pedir_vainilla():
    c = libreria.pedir_numero("ingrese numero de helados de vainilla:", 1, 100)
    print("se ha escogido", c, "helados de vainilla")
def pedir_fresa():
    c = libreria.pedir_numero("ingrese numero de helados de fresa:", 1, 100)
    print("se ha escogido", c, "helados de fresa")
def sabores():
    opc=0
    max=4
    while(opc!=max):
        print("#### sabores ####")
        print("# 1- lucuma")
        print("# 2- vainilla")
        print("# 3- fresa")
        print("# 4- salir")
        opc=libreria.pedir_numero("ingrese opcion:",1,4)
        if(opc==1):
            pedir_lucuma()
        if(opc==2):
            pedir_vainilla()
        if(opc==3):
            pedir_fresa
def pedir_lucuma_l():
    c = libreria.pedir_numero("ingrese numero de helados de lucuma con leche:", 1, 100)
    print("se ha escogido", c, "helados de lucuma con leche")
def pedir_fresa_p():
    c = libreria.pedir_numero("ingrese numero de helados de fresa con platano:", 1, 100)
    print("se ha escogido", c, "helados de fresa con platano")
def pedir_vainilla_m():
    c = libreria.pedir_numero("ingrese numero de helados de vainilla con mani:", 1, 100)
    print("se ha escogido", c, "helados de vainila con mani")
def combinados():
    opc = 0
    max = 4
    while (opc != max):
        print("#### sabores ####")
        print("# 1- lucuma con leche")
        print("# 2- vainilla con mani")
        print("# 3- fresa con platano")
        print("# 4- salir")
        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)
        if (opc == 1):
            pedir_lucuma_l()
        if (opc == 2):
            pedir_vainilla_m()
        if (opc == 3):
            pedir_fresa_p()


opc=0
max=3
# MENU PRINCIPAL
while(opc!=max):
    print("#######  HELADERIA ######")
    print("# 1.SABORES")
    print("# 2.COMBINADOS")
    print("# 3.SALIR")

    # ELECCION DE LA OPCION DEL MENU
    opc=libreria.pedir_numero("Ingrese opcion:",1,3)
    # MAPEO DE LAS OPCIONES
    if(opc==1):
        sabores()
    if(opc==2):
        combinados()


print("PROGRAMA FINALIZADO")
# FIN MENU