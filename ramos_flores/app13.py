import libreria
opc=0
max=3
while(opc!=max):
    print("#### menu ####")
    print("# 1. agregar carreras profesionales")
    print("# 2. agregar universidades")
    print("# 3. salir")

    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
