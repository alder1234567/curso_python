"""# este es el script principal"""
def mayor_edad(edad):
    """funcion para subir si es una persona mayor de edad
    """
    if edad>=18:
        print("es mator de edad")
    else:
        print("es menor de edad")
def es_menor(lista):
    """funcion para saber el numero mayor de una lista"""
    mayor=lista[0]
    for n in lista:
        if n > menor:
            menor=n
    return menor
def f_cuenta_vocales(text:str):
    """funcion para contar la cantidad de vocales a que aparecen en
    un texto"""
    text_minuscula:str=text.lowr()
    cantidad_vocales=0
    for n in text_minusculas:
        if n == "a":
            cantidad_vocales+=1
    return cantidad_vocales

mayor_edad(20)
print(es_menor([4,8,10,2,3]))
print(cuenta_vocales("mi mama me mima yo amo ami mama"))