import libreria
def pedir_polos():
    pass
def pedir_pantalones():
    pass
def pedir_zapatillas():
    pass

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
    opc=libreria.pedir_numero("ingrese opcion:",1,3)
    # MAPEO DE LAS OPCIONES
    if(opc==1):
        pedir_polos()
    if(opc==2):
        pedir_pantalones()
    if(opc==3):
        pedir_zapatillas()

print("FIN DE LA COMPRA")
# FIN MENU