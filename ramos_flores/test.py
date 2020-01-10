import libreria
assert (libreria.validar_cuadernos("justus")==True)
assert (libreria.validar_cuadernos("stanford")==True)
assert (libreria.validar_cuadernos("jkvbdsbvsv")==False)
assert (libreria.validar_cuadernos(1213)==False)
print("validar cuaderno -> ok")


assert (libreria.validar_mochilas("porta")==True)
assert (libreria.validar_mochilas(122344)==False)
assert (libreria.validar_mochilas("caterpilar - ")==False)
assert (libreria.validar_mochilas("PORTa")==False)
print("validar mochila -> ok")

assert (libreria.validar_lapiero("artesco")==True)
assert (libreria.validar_lapiero("12345")==False)
assert (libreria.validar_lapiero("faber castell")==True)
assert (libreria.validar_lapiero("pilot")==True)
print("validar lapicero -> ok")


assert (libreria.validar_edad(12)==True)
assert (libreria.validar_edad("hola")==False)
assert (libreria.validar_edad("hoal")==False)
assert (libreria.validar_edad(120)==False)
print("validar edad -> ok")


assert (libreria.validar_curso("matematica")==True)
assert (libreria.validar_curso(1213)==False)
assert (libreria.validar_curso("hola")==False)
assert (libreria.validar_curso("fisica")==True)
print("validar curso -> ok")


assert (libreria.validar_nivel("intermedio")==True)
assert (libreria.validar_nivel(1)==False)
assert (libreria.validar_nivel("hola")==False)
assert (libreria.validar_nivel("avanzado")==True)
print("validar nivel -> ok")


assert (libreria.validar_carrera("ingenieria civil")==True)
assert (libreria.validar_carrera("ingenieria electronica")==True)
assert (libreria.validar_carrera("ingenieria enferneiro")==False)
assert (libreria.validar_carrera("ingenieria de sistemas")==True)
print("validar carrera -> ok")





