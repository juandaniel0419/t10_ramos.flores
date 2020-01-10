import libreria


def opcionA():
     a=libreria.pedir_lista("zapatillas.txt")
     print("que tipo de zapatillas desea comprar ud.   ,  gracias por su compra vuelva pronto", a)

def opcionB():
    b= libreria.pedir_lista("pantalones.txt")
    print("que tipo de pantalon  desea comprar ud.   ,  gracias por su compra vuelva pronto", b)


def opcionC():
    c= libreria.pedir_lista("polos.txt")
    print("que tipo de polos desea comprar ud.   ,  gracias por su compra vuelva pronto",c)


opc=0
max=4
while(opc!=max):
    # 1. IMPRESION DEL MENU
    print("########## TIENDA DE ROPA  ########")
    print("1. opcion A")
    print("2. opcion B")
    print("3. opcion C")
    print("4. SALIR")
    print("######################")
    # 2. ELECCION DE LA OPCION  DEL MENU
    opc = libreria.pedir_numero("ingrese opcion:", 1, 4)

    # 3. MAPEO DE LAS OPCIONES
    if (opc == 1):
        opcionA()
    if (opc == 2):
        opcionB()
    if (opc == 3):
        opcionC()

