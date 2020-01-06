import libreria

def pedir_arroz():
    pass
def pedir_ceviche():
    pass
def pedir_lomo():
    pass

# ESTE PROGRAMA MUESTRA EL MENU DE UN RESTAURANT
# ESTE MENU TENDRA 4 OPCIONES
# CADA OPCION ES UN PLATO EN PARTICULAR
opc=0
max=4
#MENU GENERAL
while(opc!=max):
    print("#######  RESTAURANT \"TIA JULIA\" #######")
    print("####### 1.-Arroz Con Pollo      #######")
    print("####### 2.-Ceviche              #######")
    print("####### 3.-Lomo Saltado         #######")
    print("####### 4.-Salir                #######")
    # ELECCION DE LA OPCION DEL MENU
    opc = libreria.pedir_numero("Ingrese la opcion del Plato:", 1, 4)
    if(opc==1):
        pedir_arroz()
    if(opc==2):
        pedir_ceviche()
    if(opc==3):
        pedir_lomo()
print("FIN DEL MENU")
# FIN DEL MENU


