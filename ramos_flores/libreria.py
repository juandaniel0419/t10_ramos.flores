def validar_entero(n):
    if(isinstance(n,int)):
        return True
    else:
        return False





def validar_rango(n,ri,rf):
    if (validar_entero(n)== True):

        if (n >= ri and n <= rf):
            return True
        else:
            return False
    else:
        return False



def pedir_numero(msg,ri,rf):
    n=""
    while(validar_rango(n,ri,rf) == False):
        n=input(msg)
        if (n.isdigit()==True):
            n=int(n)
    #rin_white
    return n

#fin_pedir_numero
def pedir_nombre(msg):

    nombre=""
    while(validar_nombre(nombre)==False):
         nombre=input(msg)
    return nombre
def validar_nombre(msg):
    if(isinstance(msg,str)):
        if(len(msg)>=3):
            return True
        else:
            return False
    else:
        return False

def guardar_datos(nombre_archivo,contenido,modo):
    archivo=open(nombre_archivo,modo)
    archivo.write(contenido)
    archivo.close()


def obtener_datos(nombre_archivo):
    archivo=open(nombre_archivo)
    contenido=archivo.read()
    archivo.close()
    return contenido
