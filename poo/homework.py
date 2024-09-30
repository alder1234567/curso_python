#crear un clase banco 
#sus atributos seran nombre, apellido, dni,  bumero de cuenta y saldo inicial

#com metodo podemos hacer deposito retirar dinero y ver estado de cuenta 

class Banco:
    def __init__(self, nombre, apellido, dni, numero_cuenta, saldo_inicial=0):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo_inicial

    def deposito(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad

    def retiro(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad

    def estado_cuenta(self):
        return f"{self.nombre} {self.apellido}\nDNI: {self.dni}\nCuenta: {self.numero_cuenta}\nSaldo: {self.saldo}"

cliente = Banco("julian", "william", "12345678", "0001", 1000)
cliente.deposito(500)
cliente.retiro(200)
print(cliente.estado_cuenta())


#crear una clase de agencia
#con su nombres atributos nombre y apellido del pasjero dni numero asiento fecha  de pasaje 
#su estados seran ingresar origen , ingresar destino , cancelar viaje , ver estdo de vieaje 
class Agencia:
    def __init__(self, nombre, apellido, dni, asiento, fecha): 
        self.nombre, self.apellido, self.dni, self.asiento, self.fecha = nombre, apellido, dni, asiento, fecha
        self.origen, self.destino, self.viaje = None, None, False

    def ingresar_origen(self, origen): self.origen = origen
    def ingresar_destino(self, destino): self.destino = destino
    def cancelar_viaje(self): self.viaje = False
    def estado_viaje(self): return f"Origen: {self.origen}, Destino: {self.destino}, Estado: {'Confirmado' if self.viaje else 'Cancelado'}"

# Ejemplo de uso
viaje = Agencia("Ana", "García", "12345678", "12A", "2024-09-30")
viaje.ingresar_origen("Madrid")
viaje.ingresar_destino("Barcelona")
viaje.viaje = True  
# Confirmar viaje
print(viaje.estado_viaje())
