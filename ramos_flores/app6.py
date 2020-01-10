import libreria

def jugar_fifa():
    c=libreria.pedir_numero("ingrese numero de camiseta:",1,100)
    j=libreria.pedir_nombre("ingrese nombre del jugador:")
    print("datos guardados","el jugador",j,"tien la camiseta #",c)

def jugar_pez():
    c = libreria.pedir_numero("ingrese numero de camiseta:", 1, 100)
    j = libreria.pedir_nombre("ingrese nombre del jugador:")
    print("datos guardados", "el jugador", j, "tiene la camiseta #", c)

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
    opc=libreria.pedir_numero("Ingrese opcion:",1,2)
    # MAPEO DE LAS OPCIONES
    if(opc==1):
        jugar_fifa()
    if(opc==2):
        jugar_pez()

print("SALIENDO.....")
# fin menu
