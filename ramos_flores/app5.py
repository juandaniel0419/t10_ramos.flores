import libreria
# MENU DE UTILES
# EL MENU MOSTRARA 4 OPCCIONES QUE DEBERAN ELEGIR CON LOS NUMEROS(1-4)
def pedir_cuadernos():
    cuaderno=libreria.pedir_cuaderno("ingrese marca del cuaderno que desea:")
    print("usted ha elegido",cuaderno)

def pedir_mochila():
    mochila=libreria.pedir_mochila("ingrese la marca del la mochila que desea:")
    print("usted ha elegido",mochila)
def pedir_lapiceros():
    lapicero=libreria.pedir_lapicero("ingrese la marca del lapicero que desea:")
    print("usted ha elegido",lapicero)

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

