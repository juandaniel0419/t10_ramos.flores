import libreria
def pedir_tequeño():
    pass
def pedir_ceviche():
    pass
def pedir_choclo():
    pass
opc=0
#PROCESSING
opc=0
max=4
while(opc!=max):
    print("############ MENU #####################")
    print("#1. Entrada - Tequeño (S/2.00)        #")
    print("#2. Entrada - Ceviche (S/5.00)        #")
    print("#3. Entrada - Torta de Choclo (S/2.00)#")
    print("#4 SALIR                              #")
    print("##################################")
    opc=libreria.pedir_numero("ingrese opcion:",1,4)

    # Si el cliente pidio Tequeño, pedir la cantidad
    if ( opc == 1):
        tequeno_cant=int(input("Ingrese la cantidad de tequeños:"))
        tequeno_total=tequeno_cant*tequeno_costo
        total += tequeno_total
    #fin_if

    # SI el cliente pidio Ceviche, pedir la cantidad
    if( opc == 2 ):
        ceviche_cant=int(input("Ingrese la cantidad de ceviche:"))
        ceviche_total=ceviche_cant*ceviche_costo
        total += ceviche_total
print("fin del programa")

#fin_menu

# OUTPUT
print("#####################################")
print("# RESTAURANTE DON PEDRITO#")
print("#####################################")
print("# Cliente: JUAN")
print("+++++++++++++++++++++++++++++++++++")
print("+ Cantidad   Producto   P.U  Total+")
if ( tequeno_cant > 0 ):
    print("+ ",tequeno_cant,"          Tequeño    ",tequeno_costo,"  ",tequeno_total," +")
if (ceviche_cant > 0):
    print("+ ",ceviche_cant,"          Ceviche    ",ceviche_costo,"  ",ceviche_total," +")
print("+++++++++++++++++++++++++++++++++++")
print("+ Total: S/. ",total,"                 +")
print("+++++++++++++++++++++++++++++++++++")

