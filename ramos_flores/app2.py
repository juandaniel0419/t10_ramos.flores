import libreria
# EN ESTE MENU PODRAN ELEGIR VARIAS OPCIONES Y TAMBIEN REALIZAR SU BOLETA DE
# DE CONSUMO
def sabores():
    sabor=input("ingrese sabor:")
    print("ustded ha elegido el sabor de",sabor)
def combinados():
    sabor1=input("ingrese sabor 1:")
    sabor2=input("ingrese sabor 2:")
    print("ustded ha elegido combinar los sabores",sabor1,"y",sabor2)

opc=0
max=4
# MENU PRINCIPAL
while(opc!=max):
    print("#######  HELADERIA ######")
    print("# 1.SABORES")
    print("# 2.COMBINADOS")
    print("# 3.SALIR")

    # ELECCION DE LA OPCION DEL MENU
    opc=libreria.pedir_numero("Ingrese opcion:",1,3)
    # MAPEO DE LAS OPCIONES
    if(opc==1):
        sabores()
    if(opc==2):
        combinados()


print("PROGRAMA FINALIZADO")
# FIN MENU