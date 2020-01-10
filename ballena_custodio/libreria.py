def validar_entero(n):
    if (isinstance(n, int)):
        return True
    else:
        return False

def validar_rango(n, ri, rf):
    if ( validar_entero(n) == True):
        if (n >= ri and n <= rf):
            return True
        else:
            return False
    else:
        return False


def pedir_numero(msg,ri,rf):
    n=0
    rango_invalido=True
    while(validar_rango(n,ri,rf)==False):
        n=input(msg)
        if (n.isdigit()==True):
            n=int(n)
        #fin_if
        rango_invalido=validar_rango(n,ri,rf)
    #fin_while
    return n

def pedir_lista(msg):
    archivo=open(msg)
    datos=archivo.readlines()
    lista=[]
    for item in datos:
        lista.append(item.replace("\n",""))
    archivo.close()
    return lista