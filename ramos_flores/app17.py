import libreria
def nivel_basico():
    n=libreria.pedir_nombre("ingrese nombre que desea matricularse:")
    c=libreria.pedir_carrera("ingrese carrera:")
    print("alumno",n,"usted se matriculo en la academia sin fronteras")
def nivel_intermedio():
    n = libreria.pedir_nombre("ingrese nombre que desea matricularse:")
    c = libreria.pedir_carrera("ingrese carrera:")
    print("alumno", n, "usted se matriculo en la academia sin fronteras")
def nivel_avanzado():
    n = libreria.pedir_nombre("ingrese nombre que desea matricularse:")
    c = libreria.pedir_carrera("ingrese carrera:")
    print("alumno", n, "usted se matriculo en la academia sin fronteras")
def ing():
    n = libreria.pedir_nombre("ingrese nombre que desea matricularse:")
    c = libreria.pedir_carrera("ingrese carrera:")
    print("alumno", n, "usted se matriculo en la carrera de",c)
def emp():
    n = libreria.pedir_nombre("ingrese nombre que desea matricularse:")
    c = libreria.pedir_carrera("ingrese carrera:")
    print("alumno", n, "usted se matriculo en la carrera de",c)
def bio():
    n = libreria.pedir_nombre("ingrese nombre que desea matricularse:")
    c = libreria.pedir_carrera("ingrese carrera:")
    print("alumno", n, "usted se matriculo en la carrera de",c)


def academia():
    opc=0
    max=4
    while(opc!=max):
        print("###### ESCRIPCION PARA ACADEMIA ######")
        print("# 1.nivel basico")
        print("# 2.nivel intermedio")
        print("# 3.nivel avanzado")
        print("# 4.salir")
        opc=libreria.pedir_numero("ingrese opcion:",1,4)
        if(opc==1):
            nivel_basico()
        if(opc==2):
            nivel_intermedio()
        if(opc==3):
            nivel_avanzado()

def universidad():
    opc = 0
    max = 4
    while (opc != max):
        print("###### matricula para universidad ######")
        print("# 1.matricularse en ingenierias")
        print("# 2.matricularse en empresariales")
        print("# 3.matricularse en biomedicas")
        print("# 4.salir")
        opc = libreria.pedir_numero("ingrese opcion:", 1, 4)
        if (opc == 1):
            ing()
        if (opc == 2):
            emp()
        if (opc == 3):
            bio()


# ESTE MENU TRAE DOS OPCIONES ENTRE ACADEMIA PARA LOS QUE QUIEREN UNA NACIONAL
# Y UNIVERSIDAD PARA LOS QUE QUIEREN UNA PARTICULAR
opc=0
max=3
# MENU PRINCIPAL
while(opc!=max):
    print("############### MENU #############")
    print("# 1.Escripcion para academia     #")
    print("# 2.Escripcion para universidad  #")
    print("# 3.Salir                       #")

    # ELECCION DE LA OPCION DEL MENU
    opc=libreria.pedir_numero("ingrese opcion:",1,3)

    if(opc==1):
        academia()
    if(opc==2):
        universidad()

print("PROGRAMA FINALIZADO")
