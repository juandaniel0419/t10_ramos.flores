import libreria
def comprar_sam():
    s=libreria.pedir_nombre("ingrese nombre del comprador:")
    print("el cliente",s," comprado un celular samsug")
def comprar_huw():
    s = libreria.pedir_nombre("ingrese nombre del comprador:")
    print("el cliente", s, " comprado un celular huawei")
def comprar_app():
    s = libreria.pedir_nombre("ingrese nombre del comprador:")
    print("el cliente", s, " comprado un celular apple")
# AQUEL MENU MUESTRA LA LISTA DE TRES MARCAS DE CELULARES
# EL USUARIO TENDRA CUAL ES SU MARCA FAVORITA DESPUES LE APARECERAN LOS MODELOS DE LA MARCA ESCOGIDA

opc=0
max=4
# MENU GENERAL
while(opc!=max):
    print("######### VENTA-CELULARES ###########")
    print("# 1.SAMSUNG                         #")
    print("# 2.HUAWEI                          #")
    print("# 3.APPLE                           #")
    print("# 4.SALIR")
    # ELECCION DE LA OPCION DEL MENU
    opc=libreria.pedir_numero("ingrese su opcion:",1,4)
    # MAPEO DE LAS OPCIONES
    if(opc==1):
        comprar_sam()
    if(opc==2):
        comprar_huw()
    if(opc==3):
        comprar_app()

print("COMPRA FINALIZADA")
# FIN MENU