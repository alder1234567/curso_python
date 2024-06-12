# funciones 
matematicamente una funcion es una operacion 
que toma uno o mas valores llamados 
*argumentos* y produce un valor denominado *resultado*.
>[inote]
todos los lenguajes de programacion tiene funciones incorporadas 

(funciones internas), y funciones creado por el ususario (funciones externas)
en programacuiion una funcion es un subprograma, es una estructura que nos permite agrupar 
codigo y sus principales objetivos son:
no repetir fragmentos de codigo
reutilizar el codigo en distintos escenarios
## estructura de una funcion 
una funcion viene definida por un nombre*, sus *parametros* y sus valor de *retornos* 
una ves creada la funcion podremos solicitar su ejecusion  ,
*invocando* la funcion por su *nombre*
## definir una funcion de python 
para definir una funcion en opython primero utilizaremos la palabra reservado def seguida por erlnombre de la funcion . a continuacion especificaremos los parametros con "()"si es una funcion con parametros,"(a)" si es una funcion con parametros , si tuviera iran separados por ";"finalizaremos la linea con "," en la siguiente limea sin olvidar el identado ,comenzaremos el cuerpo . de la funcion (micro programa) que puede contener 1 o mas  sentencias , finalmente deve retornar . un resultado con l palabra reservada "return"
>{!info]
>como retorno tam,bien se puede utilizar la "funcion interna".  para depúracion de codigo  no es recomendable usuario en produccion 
print dentro una funicon es una herramineta o para comprobar si una funcion esta hacioendo su tarea correctamente 
**ejemplo**
¨¨python
def saludo ():
saludo"hola chivo"
saludo_dos="como estas"
return f"(saludo); (saludo_dos)"
print(saludo())
### invocar una funcion 
para invocar una funcion (o llamar , ejecutar) una funciuo solo tendremos que escribir el nombre de la funcion seguido por "()"parantesis, 
¨¨¨python
def saludo ():
   print("hola")
#invocando la funcion 
saludo()

##retornar un valor 
las funciones pueden retornar (o devolver) un valor 
¨¨python
def uno():
return :
uno()
¨¨
>[!warning] 
>no confundif:"print()"con "return" el valor retornado por return nos permite usuario fuera de su contexto , y "print8()"solo mostrar el literal por terminal .
**ejemplo**
el archivo *lecture.py*
## retornando multiples valores 
el secreto es hacerlo mediante un tipo de datyos estructurado 
¨¨python
 def varios():
  return 2,3,4
varios()
#retorna 
def lista ():
 return ["hoa";45]
 # retornar
 def dicc():
  return ("nombre":"jose."edad"45)
  dicc()
  # retorn("nombre":"jose","edad"45)
  dicc()

## parametros y argumentos  
si una funcion no dispuciera de bvalores de netrada no estaria limitada en su actuacion es por ello que los parametros nos permiten variar los datos que consumen una funcion parta optner distintos resultados 
**ejemp,o**
*crear una funcion que trecibe un valor numerico y retorna  su ratz cuadrada*
```python
def sqrt(valor):
   return valor**(1/2)
#nota:en este caso , el valor4 es un argumento de la funcion 
sgrt(4)
```
cuando llamo a un funcion con "argumentos", los valores de estos argumentos se copian en los correspondientes"parametros"dentro de la funcion
```python
def ejem(a,b,c):
   return a+b+c
ejm(4,5,6)
```
### argumentos nominales
en esta aproximacion los argumentos no son copiados en un orden especifico que**se asignan por nombre a cada parametro por ello nos permite editar el problema de conocer o ordenar cual es el orden de los parametros en la difinicion de la funcion .
para utilizarlo,basta con realizar una asignacion de cada argumento en la propia llamada a la funcion.
**ejemplo**
```python
def bulid_cpu(familia,num_core,fracuencia):
   print(f"""
   la cpu es de la familia(familia),
   con (num_core)cores y con una frecuencia de fracuencia de (frecuencia)""")
   # haciendo uso de argumentos nominales
   bulid_cpu(num_core,familia="intel",frecuencia=2.7)
   ### argumentos nominales 
   los argumentos son copiados en un orden especifico , en este caso debemos conocer o recordar cual es el orden de los parametros
 
  **ejemplo**
```python
def bulid_cpu(familia,num_core,fracuencia):
   print(f"""
   la cpu es de la familia(familia),
   con (num_core)cores y con una frecuencia de fracuencia de (frecuencia)""")
# haciendo uso de argumento pocisiones
bulid_cpu("intel",4,2,7)
```

## parametros por efecto
es posible especificar **valores por defecto**  en los parametros de un funcion , en el caso de que no se proporcionara un valor al argumento en la lista a la funcion , el parametro correspondiente tomara el valor definidopor efecto .
**ejemplo**
```python
def alimnos(hom,app,estado="aprobado"):

alumnos("ruth","castillo")
alumnos("ruth","castillo","desaprobado")

### desempaquetado/empaquetado de argumentos(tarea)
El empaquetado y desempaquetado de argumentos en Python es una característica poderosa que te permite trabajar con un número variable de argumentos en una función. Aquí te explico ambos conceptos:

### Empaquetado de Argumentos:
El empaquetado de argumentos te permite pasar un número variable de argumentos a una función. Puedes empaquetar los argumentos utilizando el operador * (para tuplas) o ** (para diccionarios).

#### Empaquetado de argumentos posicionales (tuplas):
python
def mi_funcion(*args):
    for arg in args:
        print(arg)

mi_funcion(1, 2, 3)  # Empaquetando los argumentos 1, 2 y 3 en una tupla args


#### Empaquetado de argumentos de palabra clave (diccionarios):
python
def mi_funcion(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mi_funcion(nombre="Juan", edad=30)  # Empaquetando los argumentos en un diccionario kwargs


### Desempaquetado de Argumentos:
El desempaquetado de argumentos te permite pasar una secuencia de argumentos a una función ya empaquetados. Esto se hace utilizando los mismos operadores * y **.

#### Desempaquetado de argumentos posicionales (tuplas):
python
def mi_funcion(a, b, c):
    print(a, b, c)

args = (1, 2, 3)
mi_funcion(*args)  # Desempaquetando los argumentos de la tupla y pasándolos a la función


#### Desempaquetado de argumentos de palabra clave (diccionarios):
python
def mi_funcion(nombre, edad):
    print(f"Nombre: {nombre}, Edad: {edad}")

kwargs = {"nombre": "Juan", "edad": 30}
mi_funcion(**kwargs)  # Desempaquetando los argumentos del diccionario y pasándolos a la función


El empaquetado y desempaquetado de argumentos son especialmente útiles cuando trabajas con funciones que pueden aceptar un número variable de argumentos, ya sea en forma de tuplas o diccionarios.




## funciones internas de python (tarea)
 1.print(): Para imprimir mensajes en la consola
python
mensaje = "Hola, mundo!"
print(mensaje)

2.len(): Para obtener la longitud de un objeto iterable (como una lista o una cadena)
python
lista = [1, 2, 3, 4, 5]
longitud = len(lista)
print("La longitud de la lista es:", longitud)

3.input(): Para recibir la entrada del usuario desde la consola.
python
nombre = input("Por favor, ingresa tu nombre: ")
print("Hola,", nombre)

4.type(): Para obtener el tipo de un objeto.
python
numero = 42
tipo = type(numero)
print("El tipo de 'numero' es:", tipo)

5.range(): Para generar una secuencia de números
python
numeros = range(5)
print(list(numeros))  # Convertimos el rango a una lista para imprimirlo

6.open(): Para abrir archivos en modo de lectura, escritura o ambos
python
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

7.sum(): Para sumar los elementos de un iterable
python
numeros = [1, 2, 3, 4, 5]
total = sum(numeros)
print("La suma de los números es:", total)

8.min() y max(): Para obtener el mínimo y el máximo de un iterable.
python
numeros = [10, 5, 8, 20, 3]
minimo = min(numeros)
maximo = max(numeros)
print("El mínimo es:", minimo)
print("El máximo es:", maximo)

9.abs(): Para obtener el valor absoluto de un número
python
numero = -42
absoluto = abs(numero)
print("El valor absoluto de", numero, "es:", absoluto)

10.str(), int(), float(), list(), tuple(), dict(), set(): Para convertir entre diferentes tipos de datos
python
cadena = "123"
numero = int(cadena)
print("El número es:", numero)