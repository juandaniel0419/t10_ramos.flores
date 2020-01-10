import libreria
# ESTE TIPO DE MENU PERMITIRA LA OPCION DE AGREGAR NOTAS Y SACAR SU PROMEDIO
def agregar_nombre():
    libreria.pedir_nombre("ingrese nombre del alumno:")
    nota1 = libreria.pedir_numero("ingrese nota1:", 0, 20)
    nota2 = libreria.pedir_numero("ingrese nota2:", 0, 20)
    nota3 = libreria.pedir_numero("ingrese nota3:", 0, 20)
    contenido = str(nota1) + "\n" + str(nota2) + "\n" + str(nota3)
    libreria.guardar_datos("inf.txt", contenido, "a")
    print("Se agregaron tres notas")
    print("se ha guardado el nombre correctamente")
def agregar_curso():
    c=libreria.pedir_curso("ingrese nombre del curso")
    print("se ha agregado el curso",c)
def sacar_promedio():
    nota1=libreria.pedir_numero("ingrese nota 1:",0,20)
    nota2=libreria.pedir_numero("ingrese nota 2:",0,20)
    promedio=(nota1+nota2)/2
    print("el promedio es:",promedio)
def agregarnota():
    opc=0
    max=3
    while(opc!=max):
        print("##### menu-agregar nota ####")
        print("#1. agregar nombre      #")
        print("#2  agregar curso       #")
        print("#3 salir                #")
        opc=libreria.pedir_numero("ingrese opcion:",1,3)

        if(opc==1):
            agregar_nombre()
        if(opc==2):
            agregar_curso()


def promedio():
    opc=0
    max=2
    while(opc!=max):
        print("#### menu-promedio ###")
        print("# 1.sacar promedio:")
        print("# 2.salir")
        opc=libreria.pedir_numero("ingrese opcion:",1,2)

        if(opc==1):
            sacar_promedio()



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

print("Programa Finalizado")
# fin menu