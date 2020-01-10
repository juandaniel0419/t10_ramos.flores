import libreria
def pedir_polos():
    c=libreria.pedir_numero("ingrese numero de polos que desea comprar:",1,1000)
    n=libreria.pedir_nombre("ingrese nombre del cliente:")
    print("el cliente",n,"ha comprado",c,"de polos")
def pedir_pantalones():
    c = libreria.pedir_numero("ingrese numero de pantalones que desea comprar:", 1, 1000)
    n = libreria.pedir_nombre("ingrese nombre del cliente:")
    print("el cliente", n, "ha comprado", c, "de pantalones")
def pedir_zapatillas():
    c = libreria.pedir_numero("ingrese numero de pares de zapatillas que desea comprar:", 1, 1000)
    n = libreria.pedir_nombre("ingrese nombre del cliente:")
    print("el cliente", n, "ha comprado", c, "de pares de zapatillas")

# ESTE MENU TENDRA TRES OPCIONES LAS CUALES SERAN TRES TIPICAS DE PRENDAS DE VESTIDO
# ELEGIR UNA OPCION ASEMEJA UNA COMPRA  (cantidad/tipios)
opc=0
max=4
# MENU GENERAL
while(opc!=max):
    print("######## MENU ###########")
    print("# 1.POLOS               #")
    print("# 2.PANTALONES          #")
    print("# 3.ZAPATILLAS          #")
    print("# 4.SALIR               #")
    print("#########################")
    # ELECCION DE LA OPCION DEL MENU
    opc=libreria.pedir_numero("ingrese opcion:",1,4)
    # MAPEO DE LAS OPCIONES
    if(opc==1):
        pedir_polos()
    if(opc==2):
        pedir_pantalones()
    if(opc==3):
        pedir_zapatillas()

print("FIN DE LA COMPRA")
# FIN MENU