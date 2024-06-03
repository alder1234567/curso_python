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
#yo como dueño de mi mascota
#deseo ver una lista de mi mascota
#para tener un resumen a con trol de ellos 
#yo como dueño de mi mascota
#deso actualizarla edad de mis mascotas 
#para tener una lista de mis mascotas         



 


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


# Crear una lista con tres diccionarios que contengan los datos de las mascotas
mascotas = [
    {"nombre": "Max", "edad": 3, "sexo": "macho", "raza": "Labrador"},
    {"nombre": "Luna", "edad": 2, "sexo": "hembra", "raza": "Golden Retriever"},
    {"nombre": "Buddy", "edad": 4, "sexo": "macho", "raza": "Poodle"}
]

# Mostrar la lista original
print("Lista original:")
for mascota in mascotas:
    print(mascota)

# Crear una copia de la lista original para no modificarla
mascotas_copia = mascotas[:]

# Editar el tercer registro cambiando la edad sin modificar la lista original
mascotas_copia[2]["edad"] = 5

# Mostrar la lista original y la lista con el tercer registro modificado
print("\nLista original:")
for mascota in mascotas:
    print(mascota)

print("\nLista con el tercer registro modificado:")
for mascota in mascotas_copia:
    print(mascota)

# Crear una lista de tus mascotas
mis_mascotas = [mascota["nombre"] for mascota in mascotas]

# Mostrar la lista de tus mascotas
print("\nMis mascotas:")
print(mis_mascotas)




# Crear una lista con tres diccionarios que contienen los datos de las mascotas
mascotas = [
    {"nombre": "Max", "edad": 3, "sexo": "macho", "raza": "Labrador"},
    {"nombre": "Luna", "edad": 2, "sexo": "hembra", "raza": "Golden Retriever"},
    {"nombre": "Buddy", "edad": 4, "sexo": "macho", "raza": "Poodle"}
]

# Agregar un cuarto diccionario a la lista
mascotas.append({"nombre": "Coco", "edad": 1, "sexo": "hembra", "raza": "Chihuahua"})

# Mostrar la lista con el cuarto diccionario
print("Lista con el cuarto diccionario:")
for mascota in mascotas:
    print(mascota)

# Crear una copia de la lista original para no modificarla
mascotas_copia = mascotas[:]

# Editar el tercer registro cambiando la edad sin modificar la lista original
mascotas_copia[2]["edad"] = 5

# Mostrar la lista original y la lista con el tercer registro modificado
print("\nLista original:")
for mascota in mascotas:
    print(mascota)

print("\nLista con el tercer registro modificado:")
for mascota in mascotas_copia:
    print(mascota)

# Crear una lista de tus mascotas
mis_mascotas = [mascota["nombre"] for mascota in mascotas]

# Mostrar la lista de tus mascotas
print("\nMis mascotas:")
print(mis_mascotas)

# Actualizar la edad de tus mascotas
nombre_mascota = "Max"  # Nombre de la mascota a actualizar
nueva_edad = 4  # Nueva edad de la mascota

for mascota in mascotas:
    if mascota["nombre"] == nombre_mascota:
        mascota["edad"] = nueva_edad

# Mostrar la lista actualizada de tus mascotas
print("\nLista actualizada de mis mascotas:")
for mascota in mascotas:
    print(mascota)










#el directorio del tecnologia jose maria arguedas 
desea actualizar el proceso academico de registro de notas de sus alumnos 
con las siguientes caracteristicas ;
los documentos podran poner las notas pero no podran editarlos 
solo los cordinadores de programa de estudios dar el acceso de edicion de notas 
previa peticion del docente solo podran poner sus notas y sus porcentajes de la acistencia sera registrada 
#yo como cordinador 
#podre dar el permiso a los docentes
#para que  ingresen  las  notas de los alumnos 
 
  
#un empresario de alquiler de autos desea guardar en un base de datos la informacion de sus veiculos ,proceso que desea 
automatizar con un sistema informatico , las acciones que pueda realizar el empresario son ver las listas de autos que tiene , podra 
tambien actualizar las listas y agregar un nuevo vehiculo

#caso de uso
#yo como empresario 
#informare sobre los alquileres de veiculos 

#programacion

class SistemaAlquilerMotos:
    def _init_(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS vehiculos (
                            id INTEGER PRIMARY KEY,
                            marca TEXT,
                            modelo TEXT,
                            año INTEGER,
                            disponible BOOLEAN
                            )''')
        self.conn.commit()

    def ver_vehiculos(self):
        self.c.execute("SELECT * FROM vehiculos")
        vehiculos = self.c.fetchall()
        for vehiculo in vehiculos:
            print(vehiculo)

    def actualizar_disponibilidad(self, vehiculo_id, disponible):
        self.c.execute("UPDATE vehiculos SET disponible=? WHERE id=?", (disponible, vehiculo_id))
        self.conn.commit()

    def agregar_vehiculo(self, marca, modelo, año):
        self.c.execute("INSERT INTO vehiculos (marca, modelo, año, disponible) VALUES (?, ?, ?, ?)",
                       (marca, modelo, año, True))
        self.conn.commit()

    def cerrar_conexion(self):
        self.conn.close()

# Uso del sistema
if _name_ == "_main_":
    sistema = SistemaAlquilerMotos("vehiculos.db")

    # Ejemplo de uso
    sistema.agregar_vehiculo("Honda", "CBR500R", 2022)
    sistema.agregar_vehiculo("Yamaha", "YZF-R3", 2021)
    sistema.ver_vehiculos()
    sistema.actualizar_disponibilidad(1, False)
    sistema.ver_vehiculos()

    sistema.cerrar_conexion()

