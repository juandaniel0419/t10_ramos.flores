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

def validar_cuadernos(msg):
    if(isinstance(msg,str)):
        if(msg=="justus"or msg=="stanford" or msg=="alpha" or msg=="loro" or msg=="vikingo" or msg=="colleges" or msg=="surco"):
            return True
        else:
            return False
    else:
        return False

def pedir_cuaderno(msg):

    cuaderno=""
    while(validar_cuadernos(cuaderno)==False):
        cuaderno=input(msg)
    return cuaderno

def validar_mochilas(msg):
    if(isinstance(msg,str)):
        if(msg=="porta"or msg=="caterpilar" or msg=="pioner" or msg=="adidas" or msg=="puma" or msg=="fiddler" or msg=="surco"):
            return True
        else:
            return False
    else:
        return False

def pedir_mochila(msg):

    mochila=""
    while(validar_mochilas(mochila)==False):
        mochila=input(msg)
    return mochila


def validar_lapiero(msg):
    if(isinstance(msg,str)):
        if(msg=="artesco"or msg=="pilot" or msg=="faber castell" or msg=="vikingo" or msg=="layconsa"):
            return True
        else:
            return False
    else:
        return False

def pedir_lapicero(msg):

    lapicero=""
    while(validar_mochilas(lapicero)==False):
        lapicero=input(msg)
    return lapicero


def validar_edad(msg):
    if(isinstance(msg,int)):
        if(msg>=0 and msg<=100):
            return True
        else:
            return False
    else:
        return False

def pedir_edad(msg):
    edad=0
    while(validar_edad(edad)==False):
        edad=input(msg)
    return edad

def validar_curso(curso):
    if(isinstance(curso,str)):
        if(curso=="matematica" or curso=="algebra" or curso=="geometria" or curso=="programcion" or curso=="fisica" or curso=="programacion II"):
            return True
        else:
            return False
    else:
        return False

def pedir_curso(msg):
    curso=""
    while(validar_curso(curso)==False):
        curso=input(msg)
    return curso


def validar_nivel(nivel):
    if(isinstance(nivel,str)):
        if(nivel=="principiante" or nivel=="intermedio" or nivel=="avanzado"):
            return  True
        else:
            return False
    else:
        return False

def pedir_nivel(msg):
    nivel=""
    while(validar_nivel(nivel)==False):
        nivel=input(msg)
    return nivel


def validar_carrera(carrera):
    if(isinstance(carrera,str)):
        if(carrera=="ingenieria civil" or carrera=="ingenieria mecanica" or carrera=="ingenieria electronica" or carrera=="ingenieria de sistemas" or carrera=="ingenieria agricola" or carrera=="ingenieria indrustrial"
        or carrera=="medicina" or carrera=="contabilidad" or carrera=="administracion"or carrera=="derecho" or carrera=="comercio" or carrera=="enfermeria" or carrera=="ingenieria computacion e informatica" or carrera=="ingenieria mecanica"
        or carrera=="comunicacion" or carrera=="educacion" or carrera=="arquitectura" or carrera=="medicina veterinaria" or carrera=="agronomia" or
        carrera=="marketing"):
            return True
        else:
            return False
    else:
        return False
def pedir_carrera(msg):
    carrera=""
    while(validar_carrera(carrera)==False):
        carrera=input(msg)
    return carrera


