import libreria
# ES UN MENU DE UN JUEGO  TIPO DE ACCION
# EN EL MENU APARECERA  4 OPCIONES DEL CUAL DEBERAS ELEGIR CON (1-4)
def continuar():
    print("cargando juego.......")
def nueva_partida():
    jugador=libreria.pedir_nombre("ingrese nombre de jugador:")
    print("Jugador:",jugador,"listo para la partida")





opc=0
max=3
# MENU GENERAL
while(opc!=max):
    print("#######  MENU-FREE FIRE ####### ")
    print("1.-Continuar")
    print("2.-Nueva Partida")
    print("3.-Salir")
    # ELECCION DE LA OPCION DEL MENU
    opc=libreria.pedir_numero("Ingrese opcion:",1,3)

    if(opc==1):
        continuar()
    if(opc==2):
        nueva_partida()


print("JUEGO TERMINADO")

print("Saliendo......")
# FIN DEL MENU