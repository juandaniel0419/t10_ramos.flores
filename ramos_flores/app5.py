import libreria
# MENU DE UTILES
# EL MENU MOSTRARA 4 OPCCIONES QUE DEBERAN ELEGIR CON LOS NUMEROS(1-4)
def pedir_cuadernos():
    pass
def pedir_mochilas():
    pass
def pedir_lapiceros():
    pass

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
        pedir_mochilas()
    if(opc==3):
        pedir_lapiceros()
print("FIN DEL MENU")
# FIN DEL MENU

