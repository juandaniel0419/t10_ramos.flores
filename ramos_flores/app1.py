import libreria
# ESTE TIPO DE MENU PERMITIRA LA OPCION DE AGREGAR NOTAS Y SACAR SU PROMEDIO
def agregarnota():
    # pedir la nota (0-20)
    # guardar los datos en el archivo info.txt
    nota1 = libreria.pedir_numero("ingrese nota1:", 0, 20)
    nota2 = libreria.pedir_numero("ingrese nota2:", 0, 20)
    nota3 = libreria.pedir_numero("ingrese nota3:", 0, 20)
    contenido =str(nota1) + "\n"+str(nota2)+"\n"+str(nota3)
    libreria.guardar_datos("inf.txt", contenido, "a")
    print("Se agregaron tres notas")


def promedio():
    #  Leer contenido de linea por liena
    archivo = open("inf.txt")
    nota1 = archivo.readline().replace("\n", "")
    nota2 = archivo.readline().replace("\n", "")
    nota3 = archivo.readline().replace("\n", "")
    prom = (int(nota1) + int(nota2) + int(nota3)) / 3
    archivo.close()
    print(prom)


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