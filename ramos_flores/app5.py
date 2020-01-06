import libreria
# MENU DE UTILES
# EL MENU MOSTRARA 4 OPCCIONES QUE DEBERAN ELEGIR CON LOS NUMEROS(1-4)
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
print("FIN DEL MENU")
# FIN DEL MENU

