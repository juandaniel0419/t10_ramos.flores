import libreria
def academia():
    a=libreria.pedir_nombre("ingrese nombre que desea matricular:")
    e=libreria.pedir_numero("ingrese edad :",0,100)
    print("SE HA MATRICULADO EL ALUMN@",a,"de edad",e,"en la academia gajel")
def universidad():
    a = libreria.pedir_nombre("ingrese nombre que desea matricular:")
    e = libreria.pedir_numero("ingrese edad :",0,100)
    print("SE HA MATRICULADO EL ALUMN@", a, "de edad", e, "en la univerisidad UNPRG")

# ESTE MENU TRAE DOS OPCIONES ENTRE ACADEMIA PARA LOS QUE QUIEREN UNA NACIONAL   
# Y UNIVERSIDAD PARA LOS QUE QUIEREN UNA PARTICULAR
opc=0
max=3
# MENU PRINCIPAL
while(opc!=max):
    print("############### MENU #############")
    print("# 1.Escripcion para academia     #")
    print("# 2.Escripcion para universidad  #")
    print("# 3.Salier                       #")

    # ELECCION DE LA OPCION DEL MENU
    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        academia()
    if(opc==2):
        universidad()

print("PROGRAMA FINALIZADO")
# FIN MENU