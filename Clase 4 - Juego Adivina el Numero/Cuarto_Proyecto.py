from random import randint

valor_aleatorio = randint(1,100)
cant_intentos = 8
numero = 0
print('\n\t\tBIENVENIDO!! \n Comencemos a Jugar!!\n')
nombre = input('Ingresar tu nombre: ')

print(f'''Muy bien "{nombre}", veamos que tan bueno eres para adivinar.
Debes decirme un numero entre el 1 y el 100.
Tendras 8 (ocho) intentos para lograrlo''')

while(cant_intentos > 0):
    numero = int(input('Ingresa tu numero: '))
    if(numero > 100 or numero < 1): 
        print('No es un numero valido, recuerda que debe ser un valor entre 1 y 100')
        continue
    else:
        cant_intentos -= 1
        if numero > valor_aleatorio: print(f'\nTu número es MAYOR, vuelve a probar suerte.\n Te quedan {cant_intentos} intentos.')
        
        elif numero < valor_aleatorio: print(f'\nTu número es MENOR, vuelve a probar suerte.\n Te quedan {cant_intentos} intentos.')
        
        else: 
            print(f'\nExcelente {nombre}!! Lo has conseguido en {8-cant_intentos} intentos. \n Gracias Por Jugar\n')
            break

if(numero != valor_aleatorio): print(f'\nLo siento {nombre} el número era {numero} y te has quedado sin intentos. Has Perdido :(\n')