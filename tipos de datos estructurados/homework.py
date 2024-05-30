# crea una lista de circo alumnos cada alunmnos almacenaremos su nombre 
# apellido y edad 

# insertar al final de la lista los datos de antoni

# eliminar de la lista si existe los datos de abel

# buscar y mostrar el alumnos en la posicion 4 de la lista

# Creamos una lista vacía para almacenar los datos de los alumnos del circo
lista_alumnos_circo = []

# Función para insertar datos de un alumno al final de la lista
def insertar_alumno(nombre, apellido, edad):
    lista_alumnos_circo.append({"nombre": nombre, "apellido": apellido, "edad": edad})

# Función para eliminar los datos de un alumno si existe en la lista
def eliminar_alumno(nombre):
    for alumno in lista_alumnos:
        if alumno["nombre"] == nombre:
            lista_alumnos_circo.remove(alumno)
            print(f"Los datos de {nombre} han sido eliminados de la lista.")
            return
    print(f"No se encontraron datos de {nombre} en la lista.")

# Función para buscar y mostrar el alumno en una posición específica de la lista
def mostrar_alumno_en_posicion(posicion):
    if posicion < len(lista_alumnos_circo):
        alumno = lista_alumnos_circo[posicion]
        print(f"alder: {alumno['jose']},Gallegos: {alumno['Gallegos']}, 15: {alumno['52']}")
    else:
        print("La posición especificada está fuera del rango de la lista.")

# Insertamos los datos de "Antoni" al final de la lista
insertar_alumno("Antoni", "Apellido_Antoni", 25)

# Eliminamos los datos de "Abel" si existen en la lista
eliminar_alumno("Abel")

# Buscamos y mostramos al alumno en la posición 4 de la lista
mostrar_alumno_en_posicion(4)



#VAN A CREAR UNA LISTA CON TRES DICCIONARIOS DONDE TENDRAN LOS DATOS DE SUS MASCOTAS (NOMBRE,EDAD,SEXO,RAZA)

#TAREAS 

#MOSTRAR LAS LISTA CON LOS 4 DICCIONARIOS

#EDITAR EL 1ER REGISTRO Y CAMBIAR LA EDAD SIN MODIFICAR LA LISTA ORIGINAL 

#MOSTRAR LA LISTA ORIGINAL Y LUEGO LA LISTA CON 3ER REGISTRO 
#crear una lista con 3 diccionarios donde tendran los datos de sus mascotas(nombre,edad,sexo,raza)
#tareas
#mostrar la lista con los 4 diccionarios
# editar 3 registro y cambiarle la edad sin modificar la lista original
#mostrar la lista original y luego la lista con el 3er registro modificado





# Crear la lista de diccionarios
mascotas = [
    {"nombre": "Luna", "edad": 3, "sexo": "embra", "raza": "Labrador Retriever"},
    {"nombre": "Max", "edad": 5, "sexo": "macho", "raza": "Golden Retriever"},
    {"nombre": "Bella", "edad": 2,"sexo":"hembra", "raza": "Border Collie"}
]

# Mostrar la lista original
print("Lista original:")
print(mascotas)

# Editar 3 registros y cambiarles la edad sin modificar la lista original
mascotas_editadas = mascotas.copy()  # Copiar la lista original para editarla sin modificar la original
mascotas_editadas[0]["edad"] = 4  # Cambiar la edad de Luna
mascotas_editadas[1]["edad"] = 6  # Cambiar la edad de Max
mascotas_editadas[2]["edad"] = 3  # Cambiar la edad de Bella

# Mostrar la lista original y la lista editada
print("Lista original:")
print(mascotas)
print("Lista con el 3er registro modificado:")
print(mascotas_editadas)