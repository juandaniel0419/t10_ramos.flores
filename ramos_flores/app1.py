import libreria
# ESTE TIPO DE MENU PERMITIRA LA OPCION DE AGREGAR NOTAS Y SACAR SU PROMEDIO
def agregarnota():
    pass
def promedio():
    pass

opc=0
max=3
#MENU PRINCIPAL
while(opc!=max):
    print("######  MENU ######")
    print("# 1.agregar nota  #")
    print("# 2.promedio      #")
    print("# 3 salir         #")

    # ELECCION DE LA OPCION DEL MENU
    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        agregarnota()
    if(opc==2):
        promedio()
# fin menu
print("Programa Finalizado")