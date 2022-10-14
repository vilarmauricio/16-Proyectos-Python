'''Definiremos los Generadores y Decoradores'''


def turno_farmacia():
    num = 1
    while True:
        yield num
        num +=1


def turno_perfumeria():
    num1 = 1
    while True:
        yield num1
        num1 +=1


def turno_cosmeticos():
    num2 = 1
    while True:
        yield num2
        num2 +=1


def imprimir_turno(letra, turno):
    print(f'\t{letra} - {turno}')
    

def mostrar_informacion(funcion, letra, turno):

    def interior():
        print('Su turno es:')
        funcion(letra, turno)
        print('Aguarde y Sera Atendido. :)')

    return interior


