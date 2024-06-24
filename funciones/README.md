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


#tipos de funciones
#funciones anonimas(funcioneslambda)
###funciones clousere
###funciones caliback

###programacion funcional
```python
lista=[5,7,8,4,1]
def num_minimo(1):
    minimo=l[0]
    for n in l:
        if n < minimo:
            minmo=n
    return minimo
    #programacion funcional 
    min(lista)
    ```
####averiguar sobre map(),filter(),teduce()


# la función `map()` en Python

La función `map()` en Python permite aplicar una función a cada elemento de un iterable (como una lista, tupla, etc.) y devuelve un iterable de resultados. Aquí están los puntos clave:

1. **Sintaxis**:
   ```python
   map(función, iterable)
   ```
   - `función`: Es la función que se aplicará a cada elemento del iterable.
   - `iterable`: Es el iterable sobre el cual se aplicará la función.

2. **Resultado**:
   - `map()` devuelve un objeto map en Python 3.x (un iterador), que debe convertirse en una lista, tupla u otro iterable para ver los resultados.

3. **Uso común**:
   - Transformación de datos: `map()` se utiliza principalmente para transformar los elementos de un iterable aplicando una función.
   - Evita bucles explícitos: Permite evitar la escritura de bucles `for` explícitos para aplicar una función a cada elemento de una colección.

4. **Funciones lambda con `map()`**:
   - A menudo, se utiliza una función lambda junto con `map()` para aplicar funciones simples de manera más concisa.

5. **Eficiencia**:
   - `map()` es eficiente en términos de código y rendimiento, especialmente para operaciones simples y directas en colecciones de datos.

### Ejemplos de uso:

- **Convertir temperaturas de Celsius a Fahrenheit**:
  ```python
  def celsius_a_fahrenheit(celsius):
      return (9/5) * celsius + 32
  
  temperaturas_celsius = [0, 10, 20, 30, 40]
  temperaturas_fahrenheit = list(map(celsius_a_fahrenheit, temperaturas_celsius))
  ```

- **Conversión de cadenas a enteros**:
  ```python
  numeros_como_cadenas = ["1", "2", "3", "4", "5"]
  numeros_como_enteros = list(map(int, numeros_como_cadenas))
  ```

- **Uso de lambda para calcular cuadrados**:
  ```python
  numeros = [1, 2, 3, 4, 5]
  cuadrados = list(map(lambda x: x ** 2, numeros))
  ```

En resumen, `map()` es una función útil para aplicar una función a cada elemento de un iterable y obtener los resultados en forma de otro iterable, facilitando así la manipulación y transformación de datos en Python de manera eficiente y clara.
Claro, te explico sobre la función `filter()` en Python.







### Función filter () en Python

La función `filter()` en Python se utiliza para filtrar elementos de un iterable (como una lista, tupla, etc.) según una función de filtrado que se define. Esta función de filtrado debe devolver `True` o `False` y `filter()` devolverá un iterable que contiene solo los elementos para los cuales la función de filtrado devuelve `True`.

### Sintaxis de `filter()`

La sintaxis general de `filter()` es:

```python
filter(función_de_filtrado, iterable)
```

- `función_de_filtrado`: Es la función que se aplica a cada elemento del iterable. Debe devolver `True` o `False`.
- `iterable`: Es el iterable (como una lista, tupla, etc.) del cual se van a filtrar los elementos.

### Características clave de `filter()`

1. **Filtrado de elementos**: `filter()` se utiliza para seleccionar elementos de un iterable basándose en una función de filtrado que se aplica a cada elemento.

2. **Devuelve un iterable**: En Python 3.x, `filter()` devuelve un objeto filter, que es un iterable. Para ver los resultados, comúnmente se convierte este objeto filter a una lista, tupla u otro tipo de iterable.

3. **Eficiencia**: Al igual que `map()`, `filter()` es eficiente porque evita la necesidad de escribir bucles explícitos para filtrar elementos.

### Ejemplos de uso de `filter()`

#### Ejemplo 1: Filtrar números impares de una lista

```python
def es_impar(numero):
    return numero % 2 != 0

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_impares = list(filter(es_impar, numeros))

print(numeros_impares)
# Output: [1, 3, 5, 7, 9]
```

En este ejemplo, `filter()` aplica la función `es_impar` a cada elemento de la lista `numeros` y devuelve una lista `numeros_impares` que contiene solo los números impares.

#### Ejemplo 2: Filtrar palabras que comienzan con una letra específica

```python
def empieza_con_letra(letra, palabra):
    return palabra.startswith(letra)

palabras = ["python", "java", "c", "javascript", "php"]
palabras_con_p = list(filter(lambda x: empieza_con_letra('p', x), palabras))

print(palabras_con_p)
# Output: ['python', 'php']
```

En este ejemplo, se utiliza una función lambda junto con `filter()` para filtrar las palabras de la lista `palabras` que comienzan con la letra 'p'.

### Notas adicionales

- **Lambda con `filter()`**: Es común utilizar funciones lambda con `filter()` para definir la función de filtrado de manera más concisa y en el lugar.

- **Iterables múltiples**: Al igual que con `map()`, `filter()` puede aceptar más de un iterable. Sin embargo, la función de filtrado debe aceptar tantos argumentos como iterables se proporcionen.

En resumen, `filter()` es una función útil en Python para seleccionar elementos de un iterable según una función de filtrado definida, facilitando así la manipulación y selección de datos de manera eficiente y legible.






### Función `reduce()` en Python

La función `reduce()` en Python proporciona una manera de aplicar una función de manera acumulativa a los elementos de un iterable, reduciéndolos a un solo valor. Aunque anteriormente era una función integrada en Python 2, en Python 3 se movió al módulo `functools`. Aquí te explico en detalle cómo funciona y cómo se usa:

1. **Función**: La función que se aplicará de manera acumulativa a los elementos del iterable.
2. **Iterable**: El iterable (como una lista, tupla, etc.) sobre el cual se aplicará la función de reducción.

### Sintaxis de `reduce()`

La sintaxis general de `reduce()` es la siguiente:

```python
from functools import reduce

reduce(función, iterable, valor_inicial)
```

- `función`: Es la función que toma dos argumentos y devuelve un solo valor. Esta función se aplicará de manera acumulativa a los elementos del iterable.
- `iterable`: Es el iterable sobre el cual se aplicará la función de reducción.
- `valor_inicial` (opcional): Es el valor inicial del acumulador. Si se proporciona, el primer argumento de la función se establece como este valor inicial en la primera llamada. Si no se proporciona, el primer elemento del iterable se usa como valor inicial y la función comienza con el segundo elemento.

### Ejemplo de uso de `reduce()`

#### Ejemplo 1: Calcular la suma de todos los elementos de una lista

```python
from functools import reduce

def suma(a, b):
    return a + b

numeros = [1, 2, 3, 4, 5]
suma_total = reduce(suma, numeros)

print(suma_total)  # Output: 15
```

En este ejemplo, `reduce()` aplica la función `suma` de manera acumulativa a los elementos de la lista `numeros`, comenzando con el primer elemento como valor inicial (por defecto), y devuelve la suma total de todos los elementos.

#### Ejemplo 2: Calcular el producto de todos los elementos de una lista

```python
from functools import reduce

def producto(a, b):
    return a * b

numeros = [1, 2, 3, 4, 5]
producto_total = reduce(producto, numeros)

print(producto_total)  # Output: 120
```

En este caso, `reduce()` aplica la función `producto` de manera acumulativa a los elementos de la lista `numeros` y devuelve el producto total de todos los elementos.

### Funciones lambda con `reduce()`

Es común utilizar funciones lambda con `reduce()` para definir la función de reducción de manera más concisa y en el lugar:

```python
from functools import reduce

numeros = [1, 2, 3, 4, 5]
producto_total = reduce(lambda x, y: x * y, numeros)

print(producto_total)  # Output: 120
```

### Notas adicionales

- **Importancia del valor inicial**: Es importante tener en cuenta que si el iterable está vacío y no se proporciona un valor inicial, `reduce()` generará un error `TypeError`.

- **Eficiencia y legibilidad**: `reduce()` puede ser menos legible en comparación con otras técnicas más simples como listas de comprensión o bucles `for`, por lo que se debe utilizar con cuidado para mantener el código claro y mantenible.

En resumen, `reduce()` es una función útil en Python para aplicar una función de manera acumulativa a los elementos de un iterable y reducirlos a un solo valor, lo que puede ser útil en diversas operaciones de procesamiento de datos donde se necesita una operación acumulativa.