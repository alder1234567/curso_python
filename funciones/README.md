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
 #retornar
 def dicc():
  return ("nombre":"jose."edad"45)
  dicc()
  #retorn("nombre":"jose","edad"45)
 