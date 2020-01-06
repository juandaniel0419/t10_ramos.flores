import libreria
def sabores():
    pass
def combinados():
    pass
def mostrar_boleta():
    pass
opc=0
max=4
# MENU PRINCIPAL
while(opc!=max):
    print("#######  HELADERIA ######")
    print("# 1.SABORES")
    print("# 2.COMBINADOS")
    print("# 3.MOSTRAR BOLETA")
    print("# 4.SALIR")

    # ELECCION DE LA OPCION DEL MENU
    opc=libreria.pedir_numero("Ingrese opcion:",1,4)
    # MAPEO DE LAS OPCIONES
    if(opc==1):
        sabores()
    if(opc==2):
        combinados()
    if(opc==3):
        mostrar_boleta()

print("PROGRAMA FINALIZADO")
