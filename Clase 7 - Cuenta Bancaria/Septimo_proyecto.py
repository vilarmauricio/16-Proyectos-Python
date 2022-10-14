from os import system

class Persona:
    
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):

    def __init__(self, nombre, apellido, cuenta, balance):
        super().__init__(nombre, apellido)
        self.cuenta = cuenta
        self.balance = balance

    def imprimir_info(self):
        system('cls')
        print('Informacion de la Cuenta:\n')
        print('Nombre: ', self.nombre.upper())
        print('Apellido: ', self.apellido.upper())
        print('nro de Cuenta: ', self.cuenta)
        print('Balance: $', self.balance)

    def depositar(self, monto):
        self.balance += monto
        

    def retirar(self, monto):
        
        if self.balance < monto:
            print('La cuenta no puede quedar negativa')
        else:
            self.balance -= monto
        

def crear_usuario():
    nombre = input('Ingresar NOMBRE: ')
    apellido = input('Ingresar APELLIDO: ')
    cuenta = input('Ingresar Nro de Cuenta: ')
    balance = int(input('Ingresar Saldo Inicial: '))
    
    usuario = Cliente(nombre, apellido, cuenta, balance)
    return usuario

def inicio():
    print('Bienvenido al Sistema Bancario')
    cliente = crear_usuario()
    cliente.imprimir_info()
    terminar = False
    while( not terminar):
        print('\nOpciones: \n\t[1] Depositar\n\t[2] Retirar\n\t[3] Salir')
        opcion = input('Seleccione una Opcion: ')
        if opcion == '1':
            monto = int(input('Monto a Depositar: '))
            cliente.depositar(monto)
            cliente.imprimir_info()
        elif opcion == '2':
            monto = int(input('Monto a Retirar: '))
            cliente.retirar(monto)
            cliente.imprimir_info()
        elif opcion == '3':
            terminar = True
    print('Gracias Por usar este Programa!')

inicio()

