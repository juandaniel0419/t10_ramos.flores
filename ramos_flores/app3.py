import libreria
# ES UN MENU DE UN JUEGO  TIPO DE ACCION
# EN EL MENU APARECERA  4 OPCIONES DEL CUAL DEBERAS ELEGIR CON (1-4)
opc=0
max=4
# MENU GENERAL
while(opc!=max):
    print("#######  MENU-FREE FIRE ####### ")
    print("1.-Continuar")
    print("2.-Nueva Partida")
    print("3.-Configuraciones")
    print("4.-Salir")
    # ELECCION DE LA OPCION DEL MENU
    opc=libreria.pedir_numero("Ingrese opcion:",1,4)

print("Saliendo......")
# FIN DEL MENU