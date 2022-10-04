'''Turnero

Area:
	Perfumeria
	Farmacia
	Cosmetico

entrega numero (generadores)

mensaje de numero de entrega (decoradores)

2 partes
numeros.py (decoradores, generadores)
principal.py (principal)'''

from re import X
import numeros
from os import system

def menu():
    system('cls')
    print('*' * 38)
    print('*' * 5,'\t\tTURNERO\t\t', '*'*5)
    print('*' * 38, '\n')
    print('\t[f] - FARMACIA')
    print('\t[C] - COSMETICOS')
    print('\t[p] - PERFUMERIA')
    print('\t[s] - SALIR\n')

    

def ingresarOpcion():
    while True:
        opcion = input('Opcion: ')
        if opcion in ['f', 'c', 'p', 's']: return opcion
        menu()


    
def inicio():
    
    opcion = 'x'
    generador_f = numeros.turno_farmacia()
    generador_c = numeros.turno_cosmeticos()
    generador_p = numeros.turno_perfumeria()

    menu()
    while opcion != 's':
        opcion = ingresarOpcion()
        if opcion == 'f':
            menu()
            turno = next(generador_f)
            impresio_informacion = numeros.mostrar_informacion(numeros.imprimir_turno, opcion.upper(), turno)
            impresio_informacion()

        elif opcion == 'c':
            menu()
            turno = next(generador_c)
            impresio_informacion = numeros.mostrar_informacion(numeros.imprimir_turno, opcion.upper(), turno)
            impresio_informacion()

        
        elif opcion == 'p':
            menu()
            turno = next(generador_p)
            impresio_informacion = numeros.mostrar_informacion(numeros.imprimir_turno, opcion.upper(), turno)
            impresio_informacion()

        
inicio()