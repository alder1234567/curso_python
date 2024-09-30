#crearuna classe de alumnos con los atributos que usted crea por conveniente
# luego instanciara a 4 alumnos

class Alumno:
    def __init__(self, nombre, edad, siglo , promedio):      
        self.nombre = nombre
        self.edad = edad
        self.siglo = siglo
        self.promedio = promedio
#metodoa
def escribir(self):
    print("estoy escribiendo")
def tarea(self , nombre_docente):
    print("haciendo la tarea de:",nombre_docente) 
def terminar_tarea(self):
    print("terminando tarea anterior")


william=Alumno("william",19,"3 periodo","15 de promedio")
print(william.edad)
jose=Alumno("jose",24,"1 periodo","15 de promedio")
print(william.siglo)
erick=Alumno("erick",18,"6 periodo","17 de promedio")
print(erick.promedio)
juan=Alumno("juan",20,"8 periodo","06 de promedio")
print(juan.nombre)
