def es_menor(lista):
    """funcion para saber el numero mayor de una lista"""
    mayor=lista[0]
    for n in lista:
        if n > menor:
            menor=n
    return menor