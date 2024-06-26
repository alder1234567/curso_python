#return devueleve valores que podre hacer uso 
#crear una funcion que retorno el numero 10 y muestre por terminal 
#si es par 
#siempre que el valor que retorna mi funcion se utilizaen mas sentencias
#o operaciones
def dies ():
    return 10
if dies()%2==0:
    print("es par")
else;
    print("es impar")
#print solo muestra por terminal


# resturn cuan do queremos que nuestra funcion devuela a retorne un 
# tipo de dato o un tipo de estructurado

#crear una funcion que se muestra el producto de dos numeros 
def producto(a,b):
    return a*b

# crear una funcion que se retorne una lista de tres numeros 
def lista_numeros():
    return [3,2,6]

#crerar un funcion que por parametro reciba un nombre y retorne un 
# mesaje de bienvenida con el nombre 
def mesnaje(nombre):
    print(f"hola",(nombre), bienvenido al chongo")
# mensaje ("jose")

#crear una funcion que reciba por parametros una lista de numeros y 
#me devuelva el numero menor ,mostrar oro terminal el valor retornado
#por la funcion
lista(4,3,6,78,7)
def min(l):
minimo=l(0)
for n in l:
    if n < minimo;
    minimo=n
return minimo
print(min(lista;))

#crear un programa que reciba un parametro el nombre yedad de una persona
#el funcion debera retornar un deccion con los datos,luego mostrar por 
#terminal el valor de retorno de el funcion 
nombre="abel"
edad=19
def persona(nom,edad):
return(
    "nombre".num,
    "edad"=edad
    )
return dict( 
    nombre=nombre
    edad=edad
    )
print(persona(nombre,edad))

##ejemplo de labda
saludo=labda n,a:f"hola, (n) ,  (a)"
print(saludo("ruth" , "castillo"))

##crea un programa anonimo que reciba un parametro una 
# lista de 5 numeros y retorne dos listas una com los 
# numerospares y otra con numeros impares 

lista_numeros = (1,2,3,4,5,6,7,8,9,10)
pares=lambda l:[n for n in lista if n%2==0]
pares=lambda l:[n for n in lista if n%2==0]
print(pares(lista))
priny(impares(lista))
  

def mensaje (m) :
    print(m)
def pedir_nombre():
    nombre=input("ingrese tu nombre")
    return nombre
mensaje(pedir_nombre())

#map
lista=[4,7,8,5,2]
map(lambda x:x+1,lista) #por defecto retorna una lista
print(nueva_lista)

#tengo una lista de alumnos que todos ellos aprobaron y pasas
#al tercer semestre
#problemaen mi lista estan con el segundo semestrepor lo 
#de semestre de 2 a 3
#filter
lista_alumnos=[

(            
         "nombre";"abel",
         "edad";36,
         "semestre";2

),
(        
        "nombre":"antonhny"
        "edad"49,
        "semestre":2

),
(       
        "nombre":"edith",
        "edad":50,
        "semestre".12

), 
  
  def objeto(e):
      if "semetre" in e:
          e["semetre"]=0["semestre"]+1
   return [                                                
       
     e
   ]
alumnos_actualzados=list(map(objeto,lista_alumnos))
print(alumnos_actulizados)      



# Lista de alumnos con información extendida
alumnos = [
    {"nombre": "abel", "edad": 36, "semestre": 2, "programa_estudio": "Ingeniería Civil"},
    {"nombre": "anthony", "edad": 40, "semestre": 2, "programa_estudio": "Matemáticas"},
    {"nombre": "edith", "edad": 50, "semestre": 2, "programa_estudio": "Historia"}
]

# Iterar sobre cada alumno y cambiar el semestre de 2 a 3
# También actualizar el programa de estudio a "Arquitectura de Plataforma"
for alumno in alumnos:
    alumno["semestre"] = 3
    alumno["programa_estudio"] = "Arquitectura de Plataforma"

# Mostrar la lista actualizada de alumnos con programa de estudio
for alumno in alumnos:
    print(f"Nombre: {alumno['nombre']}, Edad: {alumno['edad']}, Semestre: {alumno['semestre']}, Programa de Estudio: {alumno['programa_estudio']}")

#filter
#devolver los numeros pares de una lista 
lista=[4,8,2,5,7,10,6,5,3,20] 
nueva_lista=list(filter(lambda x:x%2==0,lista))
print(nueva_lista)

(            
         "nombre";"abel",
         "edad";36,
         "semestre";2

),
(        
        "nombre":"antonhny"
        "edad"49,
        "semestre":2

),
(       
        "nombre":"edith",
        "edad":50,
        "semestre".12

), 


lista_filtrada=list(filter(lambda x:x["edad"]<50,lista_alumnos))
print(lista_filtrada)










