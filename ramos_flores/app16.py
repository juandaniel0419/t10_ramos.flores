import libreria
def pedir_jugadores():
    j1=libreria.pedir_nombre("ingrese primer jugador:")
    j2=libreria.pedir_nombre("ingrese primer jugador2:")
    print("Jugador,",j1,"vs",j2)

def pedir_nivel():
    n=libreria.pedir_nivel("ingrese nivel:")
    print("el nivel este juego es de",n)


def jugar_fifa():
    opc = 0
    max = 3

    while (opc != max):
        print("######## fifa #########")
        print("# 1. jugadores #")
        print("# 2. nivel #")
        print("# 3.SALIR")
        # ELECCION DE LA OPCION DEL MENU
        opc = libreria.pedir_numero("Ingrese opcion:", 1, 3)
        # MAPEO DE LAS OPCIONES
        if (opc == 1):
            pedir_jugadores()
        if (opc == 2):
            pedir_nivel()


def jugar_pez():
    opc = 0
    max = 3

    while (opc != max):
        print("######## pez #########")
        print("# 1. jugadores #")
        print("# 2. nivel #")
        print("# 3.SALIR")
        # ELECCION DE LA OPCION DEL MENU
        opc = libreria.pedir_numero("Ingrese opcion:", 1, 3)
        # MAPEO DE LAS OPCIONES
        if (opc == 1):
            pedir_jugadores()
        if (opc == 2):
            pedir_nivel()

# ESTE ES UN MENU DE JUEGO QUE CONTIENE DOS JUEGOS DE FUTBOL
opc=0
max=3
# MENU GENERAL
while(opc!=max):
    print("######## MENU #########")
    print("# 1. Juagar FIFA 2020 #")
    print("# 2. Jugar  PEZ 2020  #")
    print("# 3.SALIR")
    # ELECCION DE LA OPCION DEL MENU
    opc=libreria.pedir_numero("Ingrese opcion:",1,3)
    # MAPEO DE LAS OPCIONES
    if(opc==1):
        jugar_fifa()
    if(opc==2):
        jugar_pez()

print("SALIENDO.....")
# fin menu
