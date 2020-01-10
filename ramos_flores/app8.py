import libreria
def pedir_tequeño():
    c=libreria.pedir_numero("ingrese cantidad de tequeños",1,100)
    print("se ha elegido",c,"de tequeños")
def pedir_ceviche():
    c=libreria.pedir_numero("ingrese cantidad de platos de ceviche",1,100)
    print("se elegio",c,"de platos de tequeños")
def pedir_choclo():
    c = libreria.pedir_numero("ingrese cantidad de choclos", 1, 100)
    print("se elegio", c, "de choclos")
opc=0
#PROCESSING
opc=0
max=4
while(opc!=max):
    print("############ MENU #####################")
    print("#1. Entrada - Tequeño (S/2.00)        #")
    print("#2. Entrada - Ceviche (S/5.00)        #")
    print("#3. Entrada - Torta de Choclo (S/2.00)#")
    print("#4. salir")
    print("##################################")
    opc=libreria.pedir_numero("ingrese opcion:",1,4)

    # Si el cliente pidio Tequeño, pedir la cantidad
    if ( opc == 1):
        pedir_tequeño()
    #fin_if

    # SI el cliente pidio Ceviche, pedir la cantidad
    if( opc == 2 ):
        pedir_ceviche()
    # SI el cliente pidio choclos,pedir la cantidad
    if(opc==3):
        pedir_choclo()

print("fin del programa")

#fin_menu


